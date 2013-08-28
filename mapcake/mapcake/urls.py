#from django.conf.urls import patterns, include, url
# Changed by me to import all the default values in url configuration
from django.conf.urls import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
# Added to enable the geodjango admin:
from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapcake.views.home', name='home'),
    # url(r'^mapcake/', include('mapcake.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
