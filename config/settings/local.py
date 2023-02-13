from .base import *
from .base import env


DEBUG = True

DATABASES = {"default": env.db()}

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE
