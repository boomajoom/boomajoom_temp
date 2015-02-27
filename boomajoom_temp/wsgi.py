"""
WSGI config for boomajoom_temp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os

import newrelic.agent
from newrelic.api.exceptions import ConfigurationError

try:
    newrelic.agent.initialize('/home/boomajoom.com/boomajoom_temp/newrelic.ini')
except ConfigurationError:
    pass
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boomajoom_temp.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

try:
    application = newrelic.agent.wsgi_application()(application)
except:
    pass