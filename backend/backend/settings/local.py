from .common import *

SECRET_KEY = '$6s+m29_-i*1s)s$gx=)xlxiw7g5&u*!h-q+%2%^ecv0#e+3b9'
DEBUG = True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3'
    }
}

