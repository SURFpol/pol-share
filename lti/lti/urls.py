from django.conf.urls import url
from django.contrib import admin

from lti import views


urlpatterns = [
    url(r'^$', views.main, name="lti-main"),
    url(r'^config.xml$', views.config, name="lti-config"),
    url(r'^admin/', admin.site.urls),

]
