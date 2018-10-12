from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse

from lti.contrib.django import DjangoToolProvider

from ims.models import LTIApp


@csrf_exempt
def lti_launch(request, slug):
    print(slug, request.POST.dict())
    return redirect('share:common-cartridge-upload')


def lti_config(request, slug):
    app = LTIApp.objects.get(slug=slug)
    return TemplateResponse(request, "ims/lti_basic_config.xml", {
        "server_host": request.META['SERVER_NAME'],
        "server_port": request.META['SERVER_PORT'],
        "app": app
    })
