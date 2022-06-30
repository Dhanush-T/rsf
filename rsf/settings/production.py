from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass

AUTHENTICATION_BACKENDS = [
    "rsf.auth.IMAPAuthentication",
]
