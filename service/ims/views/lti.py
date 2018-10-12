from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse


@csrf_exempt
def lti_launch(request, lti):
    print(lti, request.POST.dict())
    return redirect('share:common-cartridge-upload')


def lti_config(request, lti):
    print(lti)
    return TemplateResponse(request, "ims/lti_basic_config.xml", {
        "server_host": request.META['SERVER_NAME'],
        "server_port": request.META['SERVER_PORT']
    })
