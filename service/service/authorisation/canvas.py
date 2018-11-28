from social_core.backends.oauth import BaseOAuth2


class CanvasOAuth2(BaseOAuth2):

    name = 'canvas-oauth2'
    AUTHORIZATION_URL = 'https://canvas.surfpol.nl/login/oauth2/auth'
    ACCESS_TOKEN_URL = 'https://canvas.surfpol.nl/login/oauth2/token'
    ACCESS_TOKEN_METHOD = 'POST'

    def get_key_and_secret(self):
        # TODO: these keys should come from the Tenant, but how to get to the Tenant?
        print(self.strategy)
        return '10000000000001', 'otqEQ706YXXZyHn2sNMQHuz9gHssC06UMWRdmZ7i45PCHOZt5evmrZeotl8OWAFW'

    def get_user_details(self, response):
        username = response.get('user', {}).get('name', None)
        return {
            'username': username,
            'email': None,
            'fullname': None,
            'first_name': None,
            'last_name': None
        }
