from .base import *
from .base import env

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DEBUG = True

DATABASES = {"default": env.db()}

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
