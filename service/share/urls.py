from django.conf.urls import url

from share.views import CommonCartridgeUploadView, CommonCartridgeDetailView


urlpatterns = [
    url(r'^upload/?$', CommonCartridgeUploadView.as_view(), name="common-cartridge-upload"),
    url(r'^upload/success/(?P<pk>[0-9]+)/?$', CommonCartridgeDetailView.as_view(),
        name="common-cartridge-upload-success"),
]
