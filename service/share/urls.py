from django.conf.urls import url
from django.contrib.auth import views as auth_views

from share.views import CommonCartridgeUploadView, CommonCartridgeDetailView


urlpatterns = [
    url(r'^upload/?$', CommonCartridgeUploadView.as_view(), name="common-cartridge-upload"),
    url(r'^upload/success/(?P<pk>[0-9]+)/?$', CommonCartridgeDetailView.as_view(),
        name="common-cartridge-upload-success"),
    url(r'^exit/?$', auth_views.LogoutView.as_view(), name="share-exit"),
]
