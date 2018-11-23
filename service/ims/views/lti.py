from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login

from lti.contrib.django import DjangoToolProvider

from ims.authorization import LTIRequestValidator
from ims.models import LTIApp, LTIPrivacyLevels, LTITenant


@csrf_exempt
def lti_launch(request, slug):
    app = get_object_or_404(LTIApp, slug=slug)
    tool_provider = DjangoToolProvider.from_django_request(request=request)
    validator = LTIRequestValidator()
    ok = tool_provider.is_valid_request(validator)
    if not ok:
        return HttpResponseForbidden('The launch request is considered invalid')
    if app.privacy_level != LTIPrivacyLevels.ANONYMOUS:
        user = authenticate(request, remote_user=request.POST.get("lis_person_contact_email_primary"))
        if user is not None:
            login(request, user)
            tenant = LTITenant.objects.get(  # launch would not be ok if DoesNotExist
                client_key=tool_provider.consumer_key
            )
            tenant.start_session(request)
    return redirect(app.view)


def lti_config(request, slug):
    app = get_object_or_404(LTIApp, slug=slug)
    return TemplateResponse(request, "ims/lti_basic_config.xml", {
        "host": request.get_host(),
        "app": app
    })
