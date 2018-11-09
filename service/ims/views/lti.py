import requests
from jose import jwt, jwk

from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login

from lti.contrib.django import DjangoToolProvider

from ims.authorization import LTIRequestValidator
from ims.models import LTIApp, LTIPrivacyLevels


PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu4UelezAtzN4D+3ZDbTT
BOpsdKuuGd35R7D0HML05df6Xmjxww3bkhBzx21J1BYyk0tcIdbFIWLV9+hyAWmZ
bhJiX0BL0kak9xhPGiCpQ2Q1xMxgz+Qg40qN1uFk+Ho4OhprOCgGgbKIYN5lRyWe
zjaS2/oXcWAuNzdA5xJVAsyUWCJ9SGqkhBsO0icBNpY0Y5RW2TyMlCo9/8kKW7jh
LH6ySiNqmcIwvzg8x+uWdqlTd9fhbA+zwlPFsVKVTcQphdPqS2ZP0h9Eo5aHLZ8B
NnMgJ3qAcMVm9soZl6d5VBhLJ1iwmAmCMQNJL3oW6K+sQQwNNPHFZKylhiQHNUEH
vQIDAQAB
-----END PUBLIC KEY-----'''


WELL_KNOWN_URL = "https://lti-ri.imsglobal.org/platforms/71/platform_keys/66.json"


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
    return redirect(app.view)


@csrf_exempt
def lti_jwt_launch(request, slug):
    app = get_object_or_404(LTIApp, slug=slug)
    jwt_token = request.POST.get("id_token", None)
    if jwt_token is None:
        return HttpResponseForbidden('The JWT launch request is missing a JWT')
    # well_known = requests.get(WELL_KNOWN_URL)
    # key = jwk.construct(well_known.json()["keys"][0])
    # print(key)
    payload = jwt.decode(
        jwt_token,
        PUBLIC_KEY,
        algorithms='RS256',
        audience='surf'  # this will be the oauth_id
    )
    # TODO: use OIDC
    # TODO: use well-known and JWK
    # Payload checks: nonce + expire
    return redirect(app.view)


def lti_config(request, slug):
    app = get_object_or_404(LTIApp, slug=slug)
    return TemplateResponse(request, "ims/lti_basic_config.xml", {
        "host": request.get_host(),
        "app": app
    })
