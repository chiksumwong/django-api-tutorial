from .settings import *

DEBUG = True

ALLOWED_HOSTS = []

# CORS
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_project',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}

# Add for Front-end
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'client/dist/static'),
]

# Files - For File and Image Upload
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")