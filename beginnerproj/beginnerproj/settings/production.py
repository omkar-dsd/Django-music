import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = True
DATABSES = settings.DATABASES

import dj_database_url
DATABASES['default'] = dj_database_url.config()

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

import os
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# STATIC_ROOT = 'staticfiles'
# STATIC_URL = '/music/static/'

# STATICFILES_DIRS = (
# 	os.path.join(BASE_DIR, 'static'),
# )

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'music/static'),
)
