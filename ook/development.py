from ook.settings import *
import os

DEBUG=True
TEMPLATE_DEBUG=DEBUG

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "media")
MEDIA_URL = "/media"

DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'devel.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
}

TEMPLATE_DIRS = (
	os.path.join(os.path.dirname(__file__), "templates"),
)