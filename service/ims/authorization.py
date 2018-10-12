from oauthlib.oauth1 import RequestValidator

from ims.models import LTICredentials


class LTIRequestValidator(RequestValidator):

    def get_client_secret(self, client_key, request):
        credentials = LTICredentials.objects.get(client_key=client_key)
        return credentials.client_secret

    def validate_client_key(self, client_key, request):
        try:
            LTICredentials.objects.get(client_key=client_key)
            return True
        except LTICredentials.DoesNotExist:
            return False
