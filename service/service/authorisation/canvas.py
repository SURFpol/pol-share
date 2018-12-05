from social_core.backends.oauth import BaseOAuth2

from ims.models import LTITenant


class CanvasOAuth2(BaseOAuth2):

    name = 'canvas-oauth2'
    AUTHORIZATION_URL = 'https://canvas.surfpol.nl/login/oauth2/auth'
    ACCESS_TOKEN_URL = 'https://canvas.surfpol.nl/login/oauth2/token'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_key_and_secret(self):
        tenant_key = self.strategy.request.session.get('tenant_key')
        if not tenant_key:
            return None, None
        tenant = LTITenant.objects.get(client_key=tenant_key)
        return tenant.api_key, tenant.api_secret

    def get_user_details(self, response):
        username = response.get('user', {}).get('name', None)
        return {
            'username': username,
            'email': None,
            'fullname': None,
            'first_name': None,
            'last_name': None
        }
