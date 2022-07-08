from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from vtvsn import views as vtvsn_views
from vtvsn import urls as vtvsn_urls
from django.conf.urls import include


urlpatterns = [
    url(r'^$', vtvsn_views.Homepage, name='Home'),
    url(r'^vtvsn/', include(vtvsn_urls)),
    url('admin/', admin.site.urls),
]


