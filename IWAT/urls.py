from django.conf.urls.defaults import *
from login.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^login/$', 'login.views.login_user'),)