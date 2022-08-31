from pickle import TRUE
from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = TRUE

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!@#lo&ifnz1a(vk=&eoa*a-$h&us-k^9brf#%_67l(1g_1&qlt"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass

AUTHENTICATION_BACKENDS = [
    "rsf.auth.DevAuthentication",
]
