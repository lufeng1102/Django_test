from django.conf.urls.defaults import patterns, include, url
from training.views import *
import settings

# import admin contrib 
from django.contrib import  admin
admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_apps.views.home', name='home'),
    # url(r'^django_apps/', include('django_apps.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', main_page),
    url(r'^$', index_page),
    url(r'^employee/(\w+)/$', employee_page),
    url(r'^books/$', book_list_page),
    # show image,css,js
    url(r'^(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),

)
