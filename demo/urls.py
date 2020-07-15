from django.conf.urls import url
from django.contrib import admin
from .views import attrs, index, metadata, one_tap_login
admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^attrs/$', attrs, name='attrs'),
    url(r'^metadata/$', metadata, name='metadata'),
    url(r'^one-tap-login$', one_tap_login, name='onetaplogin')
]
