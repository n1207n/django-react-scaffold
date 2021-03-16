from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '%s' % os.getenv('POSTGRES_DB'),
        'USER': '%s' % os.getenv('POSTGRES_USER'),
        'PASSWORD': '%s' % os.getenv('POSTGRES_PASSWORD'),
        'HOST': '%s' % os.getenv('POSTGRES_HOST'),
        'PORT': 5432,
    }
}

# CORS
CORS_ALLOWED_ORIGINS = [
    "https://example.com:9000",
    "https://api.example.com:9000",
    "https://app.example.com:9000",
    "http://localhost::9000",
    "http://127.0.0.1::9000"
]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]
CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]

# Only kicks in when there is no cloud storage being used
UPLOADS_DIR_NAME = 'uploads'
MEDIA_URL = '/%s/' % UPLOADS_DIR_NAME
MEDIA_ROOT = os.path.join(RUNTIME_VOLUME, '%s' % UPLOADS_DIR_NAME)

FILE_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 2000  # 2GB
STATIC_ROOT = '%s/staticserve' % RUNTIME_VOLUME

# Update DEBUG-sensitive setting values
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG
INSTALLED_APPS += ['debug_toolbar', ]
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
GRAPHENE['MIDDLEWARE'] += ['graphene_django.debug.DjangoDebugMiddleware', ]

# Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if SENDGRID_API_KEY:
    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
    SENDGRID_SANDBOX_MODE_IN_DEBUG = True
    SENDGRID_ECHO_TO_STDOUT = True
    DEFAULT_FROM_EMAIL = 'Admin <noreply@dev.example.com>'


# Health check
HEALTH_CHECK = {
    'DISK_USAGE_MAX': 90,  # percent
    'MEMORY_MIN': 100,    # in MB
}