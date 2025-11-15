from .base import *

DEBUG = True

CSRF_TRUSTED_ORIGINS =['http://127.0.0.1',]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*a=7ko9_+b0g69m%v4z46@47ym*5bs4)-rvc+a4r3s43jef6tm"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

# ManifestStaticFilesStorage is recommended in production, to prevent
# outdated JavaScript / CSS assets being served from cache
# (e.g. after a Wagtail upgrade).
# See https://docs.djangoproject.com/en/5.2/ref/contrib/staticfiles/#manifeststaticfilesstorage
#STORAGES["staticfiles"]["BACKEND"] = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

try:
    from .local import *
except ImportError:
    pass
