from django.template.response import TemplateResponse
from django.http import HttpResponse


def main(request):
    return HttpResponse("Hello world!")


def config(request):
    return TemplateResponse(request, "lti/config.xml")
