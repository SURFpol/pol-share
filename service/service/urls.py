from django.conf.urls import url, include
from django.contrib import admin

from share.views import UploadView, upload_success


urlpatterns = [
    url(r'', include("lti.urls", namespace="lti")),
    url(r'^upload/?$', UploadView.as_view(), name="share-upload"),
    url(r'^upload/success/?$', upload_success, name="share-upload-success"),
    url(r'^admin/', admin.site.urls),
]
