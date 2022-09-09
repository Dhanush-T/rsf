from pickle import TRUE
from .base import *

AUTHENTICATION_BACKENDS = [
    "rsf.auth.RequestAuthentication",
]

DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

WAGTAIL_ENABLE_UPDATE_CHECK = False

BASE_URL = os.getenv("BASE_URL")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE"),
        "NAME": os.environ.get("SQL_DATABASE"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
    }
}

try:
    from .local import *
except ImportError:
    pass
