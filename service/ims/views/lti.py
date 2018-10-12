from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse

from lti.contrib.django import DjangoToolProvider

from ims.authorization import LTIRequestValidator
from ims.models import LTIApp


@csrf_exempt
def lti_launch(request, slug):
    app = get_object_or_404(LTIApp, slug=slug)
    tool_provider = DjangoToolProvider.from_django_request(request=request)
    validator = LTIRequestValidator()
    ok = tool_provider.is_valid_request(validator)
    if ok:
        return redirect(app.view)
    else:
        return HttpResponseForbidden()


def lti_config(request, slug):
    app = get_object_or_404(LTIApp, slug=slug)
    return TemplateResponse(request, "ims/lti_basic_config.xml", {
        "host": request.get_host(),
        "app": app
    })
