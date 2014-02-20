from django.conf.urls import patterns, url
from django.contrib import admin

from formulario import views


admin.autodiscover()

urlpatterns = patterns('',
            url(r'form-um/$', views.formUm, name='form1'),
            url(r'form-user/$', views.formUser, name='form-user'),
)
