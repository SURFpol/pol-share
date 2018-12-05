from django.conf.urls import url
from django.contrib.auth import views as auth_views

from share.views import CommonCartridgeUploadView, CommonCartridgeDetailView, CommonCartridgeFetchViewset


urlpatterns = [
    url(r'^fetch/?$', CommonCartridgeFetchViewset.login, name="common-cartridge-fetch"),
    url(r'^fetch/start/?$', CommonCartridgeFetchViewset.start, name="common-cartridge-fetch-start"),
    url(r'^upload/?$', CommonCartridgeUploadView.as_view(), name="common-cartridge-upload"),
    url(r'^common-cartridge/detail/(?P<pk>[0-9]+)/?$', CommonCartridgeDetailView.as_view(),
        name="common-cartridge-detail"),
    url(r'^exit/?$', auth_views.LogoutView.as_view(), name="share-exit"),
]
