from .common import *

# SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
DEBUG = True
ALLOWED_HOSTS = ['*', ]
STATIC_ROOT = BASE_DIR.parent / "static"
MEDIA_ROOT = BASE_DIR.parent / 'media'
print(STATIC_ROOT)
print(MEDIA_ROOT)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '../config/my.cnf',
        },
    }
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
