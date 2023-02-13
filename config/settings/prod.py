from .base import *
from .base import env


DEBUG = False

ADMINS = [
    ("Thierry Chappuis", "email@exemple.com"),
]

ALLOWED_HOSTS = ["68.183.220.149", "wepynaire.placepython.ch"]

DATABASES = {
    "default": env.db(),
}

REDIS_URL = env("REDIS_URL", default="redis://localhost:6379")
CACHES["default"]["LOCATION"] = REDIS_URL
CHANNEL_LAYERS["default"]["CONFIG"]["hosts"] = [REDIS_URL]

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
