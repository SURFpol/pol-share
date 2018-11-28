from django.conf import settings

from datagrowth.resources import HttpResource


class CanvasResource(HttpResource):

    def auth_parameters(self):  # TODO: get access_token from social_auth and add as Bearer header
        return {
            'access_token': settings.CANVAS_ACCESS_KEY
        }

    class Meta:
        abstract = True


class CanvasIMSCCExport(CanvasResource):
    URI_TEMPLATE = 'https://{}/api/v1/users/{}/content_exports'

    def get_progress_url(self):
        if not self.success:
            return
        content_type, data = self.content
        return data.get('progress_url', None)
