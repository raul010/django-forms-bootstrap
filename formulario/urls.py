from django.conf.urls import patterns, include, url
from django.contrib import admin

from formulario import views


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'/^', include(views.formUser, namespace='formUser')),
    url(r'$', views.formUser, name='formUser'),
)
