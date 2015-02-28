# ===========
# = Imports =
# ===========

import os

# ===============
# = Directories =
# ===============
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '../static/'),
)

MEDIA_ROOT = (
    os.path.join(os.path.dirname(__file__), '../media/').replace('\\', '/')
)

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '../templates').replace('\\', '/'),)

STATIC_ROOT = os.path.join(os.path.dirname(__file__), '../assets/')

# ==========
# = Global =
# ==========

SITE_ID = 1

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

ALLOWED_HOSTS = []

# ============
# = Security =
# ============

DEBUG = True
TEMPLATE_DEBUG = True

INVITE_CODE = u'42'

SECRET_KEY = 'totally_secret'  # overriden in local_settings
CSRF_COOKIE_NAME = 'brf'

# ================
# = Applications =
# ================

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'debug_toolbar',
    'django_nose',
    'core',
    'about',
)

# ===================
# = Django Specific =
# ===================

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)



WSGI_APPLICATION = 'boomajoom_temp.wsgi.application'

# ===================
# = URL's and Paths =
# ===================

ROOT_URLCONF = 'boomajoom_temp.urls'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# ===========
# = Testing =
# ===========

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=core,about',
]

# ============
# = Database =
# ============

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'boomajoom',
        'USER': 'boomajoom',
        'PASSWORD': 'boomajoom',
        'HOST': 'localhost'
    }
}

# DO NOT COMMENT BELOW LINE WHEN COMMITTING.

try:
    from boomajoom_temp.local_settings import *
except ImportError:
       pass

