from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.template.response import TemplateResponse
from django.shortcuts import HttpResponse

from datagrowth.resources.http.tasks import send
from share.models import CommonCartridgeShared, CommonCartridgeSharedForm


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
        social_auth = request.user.social_auth.last()
        access_token = social_auth.access_token
        course_id = request.session.get('course_id', None)
        api_domain = request.session.get('api_domain', None)
        roles = request.session.get('roles', '').split(',')
        if not 'Instructor' in roles or not course_id or not access_token or not api_domain:
            return HttpResponse('forbidden')
        config = {
            "resource": "share.CanvasIMSCCExport",
            "purge_immediately": True,
            "continuation_limit": 30,
            "interval_duration": 1000,
            "_access_token": access_token,
            "_namespace": "http_resource",
            "_private": ["_private", "_namespace", "_defaults"]
        }
        scc, err = send(api_domain, course_id, export_type='common_cartridge', config=config, method='post')

        return HttpResponse('success')
