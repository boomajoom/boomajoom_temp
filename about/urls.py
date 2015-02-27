from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^privacy-policy/$', 'about.views.privacy_policy', name='privacy_policy'),
                       url(r'^terms-of-service/$', 'about.views.terms_of_service', name='terms_of_service'),
                       )