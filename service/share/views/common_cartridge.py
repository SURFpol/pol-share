from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.template.response import TemplateResponse
from django.shortcuts import redirect, reverse, HttpResponse

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
        print("Access token:", access_token)
        print(request.session.keys())
        print(request.session.values())
        # TODO: Should make an API call that gets the CommonCartridge
        return HttpResponse('success')
