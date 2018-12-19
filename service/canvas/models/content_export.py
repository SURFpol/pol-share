import os
from copy import deepcopy
from urlobject import URLObject

from django.db.models import signals

from datagrowth.resources import HttpResource, HttpFileResource, file_resource_delete_handler


class CanvasResource(HttpResource):

    def auth_headers(self):
        # TODO: current setup stores access_tokens in a unencrypted db, which is wrong.
        # Configurations should be able to delegate values to other objects (like social_auth models)
        if not self.config.access_token:
            return {}
        return {
            "Authorization": "Bearer {}".format(self.config.access_token)
        }

    class Meta:
        abstract = True


class CanvasIMSCCExport(CanvasResource):
    URI_TEMPLATE = 'https://{}/api/v1/courses/{}/content_exports'

    def get_progress(self):
        if not self.success:
            return None, None
        content_type, data = self.content
        return data.get('id', None), data.get('workflow_state', None)

    def get_download_url(self):
        export_id, workflow_state = self.get_progress()
        if not workflow_state == 'exported':
            return None
        content_type, data = self.content
        attachment = data.get('attachment', {})
        return attachment.get('url', None)

    @staticmethod
    def get_continuation_url(request, export_id):
        url = URLObject(request.get("url"))
        tail, head = os.path.split(url.path)
        if head == 'content_exports':
            head += '/{}'.format(export_id)
        url = url.with_path(os.path.join(tail, head))
        return str(url)

    def create_next_request(self):

        export_id, workflow_state = self.get_progress()
        if not self.success or workflow_state == 'exported':
            return None

        request = deepcopy(self.request)
        request["method"] = "get"
        request["url"] = self.get_continuation_url(request, export_id)
        return request

    def close(self):
        export_id, workflow_state = self.get_progress()
        if not self.success or workflow_state == 'exported':
            super().close()


class CanvasIMSCCExportDownload(HttpFileResource):
    pass


signals.post_delete.connect(file_resource_delete_handler, sender=CanvasIMSCCExportDownload)
