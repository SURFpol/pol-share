from django.views.generic.edit import CreateView
from django.http.response import HttpResponse

from ims.models import CommonCartridge, CommonCartridgeForm


class UploadView(CreateView):
    model = CommonCartridge
    template_name = 'share/upload.html'
    success_url = '/upload/success/'
    form_class = CommonCartridgeForm


def upload_success(request):
    return HttpResponse('upload success')
