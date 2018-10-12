from django.conf.urls import url, include
from django.contrib import admin

from ims import views as ims_views


urlpatterns = [
    url(r'share/', include("share.urls", namespace="share")),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[A-Za-z0-9\-]+)/config.xml$', ims_views.lti_config),
    url(r'^(?P<slug>[A-Za-z0-9\-]+)/?$', ims_views.lti_launch)
]
