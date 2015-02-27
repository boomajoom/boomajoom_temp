from __future__ import absolute_import

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'core.views.index_page', name='index_page'),
                       # about urls
                       url(r'^about/', include('about.urls')),
                       # admin urls
                       url(r'^admin/', include(admin.site.urls)),
                       # feedback urls
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))