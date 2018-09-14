from django.conf.urls import url

from lti import views


urlpatterns = [
    url(r'^$', views.main, name="main"),
    url(r'^config.xml$', views.config, name="config")
]
