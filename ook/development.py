from ook.settings import *
import os

DEBUG=True
TEMPLATE_DEBUG=DEBUG

MEDIA_ROOT = os.path.join(PROJECT_DIR, 'tmp', 'media')
MEDIA_URL = "/media"

DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR, 'tmp', 'db', 'devel.db'),              # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
}

TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), "templates"),
)

INSTALLED_APPS += [ 'debug_toolbar', ]

USERENA_ACTIVATION_REQUIRED = False