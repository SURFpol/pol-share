from django.views.generic.edit import CreateView
from django.http.response import HttpResponse

from ims.models import CommonCartridge


class UploadView(CreateView):
    model = CommonCartridge
    fields = ['file']
    template_name = 'share/upload.html'
    success_url = '/upload/success/'


def upload_success(request):
    return HttpResponse('upload success')
