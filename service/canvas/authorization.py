from social_core.backends.oauth import BaseOAuth2

from ims.models import LTITenant


class CanvasOAuth2(BaseOAuth2):
    """
    This class provides OAuth2 authentication with the Canvas API.
    It assumes that the user is in a LTI session that has been started by the django_ims_toolkit package
    """

    name = 'canvas-oauth2'
    AUTHORIZATION_URL = 'https://{}/login/oauth2/auth'
    ACCESS_TOKEN_URL = 'https://{}/login/oauth2/token'
    ACCESS_TOKEN_METHOD = 'POST'

    def authorization_url(self):
        canvas_api_domain = self.strategy.request.session.get('api_domain', None)
        assert canvas_api_domain, 'Expected the Canvas LTI launch to set api_domain on session'
        return self.AUTHORIZATION_URL.format(canvas_api_domain)

    def access_token_url(self):
        canvas_api_domain = self.strategy.request.session.get('api_domain', None)
        assert canvas_api_domain, 'Expected the Canvas LTI launch to set api_domain on session'
        return self.ACCESS_TOKEN_URL.format(canvas_api_domain)

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
