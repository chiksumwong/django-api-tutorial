from .settings import *

DEBUG = True

ALLOWED_HOSTS = []

# CORS
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8080'
]

# SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# # MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'django_project',
#         'USER': 'root',
#         'PASSWORD': '',
#         'HOST': '127.0.0.1',
#         'PORT': '3306'
#     }
# }

# Add for Front-end
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'client/dist/static'),
]

# Files - For File and Image Upload
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Social Login - Google
GOOGLE_CLIENT_ID = ''


# Social Login - Facebook
FACEBOOK_CLIENT_ID = ''
FACEBOOK_CLIENT_SECRET = ''
