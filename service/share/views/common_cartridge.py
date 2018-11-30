from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from datagrowth.configuration import create_config
from datagrowth.resources.http.tasks import send
from share.models import CommonCartridgeShared, CommonCartridgeSharedForm, CanvasIMSCCExport, CanvasIMSCCExportDownload


class CommonCartridgeUploadView(CreateView):
    model = CommonCartridgeShared
    template_name = 'share/common_cartridge/upload.html'
    form_class = CommonCartridgeSharedForm


class CommonCartridgeDetailView(DetailView):
    model = CommonCartridgeShared
    template_name = 'share/common_cartridge/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["metadata"] = self.object.get_metadata()
        return context


class CommonCartridgeFetchViewset(object):

    @staticmethod
    def login(request):
        return TemplateResponse(request, 'share/common_cartridge/login.html', {})

    @staticmethod
    def start(request):

        # Checking authentication and preparing download
        social_auth = request.user.social_auth.last()
        access_token = social_auth.access_token
        course_id = request.session.get('course_id', None)
        api_domain = request.session.get('api_domain', None)
        roles = request.session.get('roles', '').split(',')
        if not 'Instructor' in roles or not course_id or not access_token or not api_domain:
            return HttpResponseForbidden(
                'You are not an Instructor or one of course_id, access_token and/or api_domain is not set properly'
            )

        # Create the IMSCC export through the API
        config = create_config('http_resource', {
            "resource": "share.CanvasIMSCCExport",
            "purge_immediately": True,
            "continuation_limit": 30,
            "interval_duration": 1000,
            "_access_token": access_token,
        })
        scc, err = send(api_domain, course_id, export_type='common_cartridge', config=config, method='post')
        success = next((_id for _id in scc if _id), None)
        if success is None:
            return HttpResponse('could not create IMSCC export through Canvas API')

        # Download the IMSCC export
        canvas_export = CanvasIMSCCExport.objects.get(id=success)
        download_url = canvas_export.get_download_url()
        download = CanvasIMSCCExportDownload(config=config).get(download_url)
        download.close()
        if not download.success:
            return HttpResponse('could not download IMSCC export')
        content_type, imscc_file = download.content
        imscc = CommonCartridgeShared.from_file_path(imscc_file.file.name)
        imscc.save()

        return redirect(imscc)
