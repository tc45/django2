from .base import *

DEBUG = True
ALLOWED_HOSTS = ['django_starter.ddns.net', 'localhost', '127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
