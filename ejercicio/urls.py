from django.conf.urls import patterns, include, url

from django.contrib import admin
from stockapp import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ejercicio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'stockapp.views.index', name='index'),
    url(r'^list_items/$', 'stockapp.views.list_items', name='list_items'),
)
