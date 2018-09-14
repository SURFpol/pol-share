from django.template.response import TemplateResponse
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hello world!")


def config(request):
    return TemplateResponse(request, "service/config.xml", {
        "server_host": request.META['SERVER_NAME'],
        "server_port": request.META['SERVER_PORT']
    })
