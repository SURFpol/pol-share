from django.conf.urls import url, include
from django.contrib import admin

from share.views import CommonCartridgeUploadView, CommonCartridgeDetailView


urlpatterns = [
    url(r'', include("lti.urls", namespace="lti")),
    url(r'^upload/?$', CommonCartridgeUploadView.as_view(), name="common-cartridge-upload"),
    url(r'^upload/success/(?P<pk>[0-9]+)/?$', CommonCartridgeDetailView.as_view(),
        name="common-cartridge-upload-success"),
    url(r'^admin/', admin.site.urls),
]
