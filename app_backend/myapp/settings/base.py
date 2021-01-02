import os
import sys
from datetime import timedelta
from pathlib import Path

# Load env variables to start
ENV = os.getenv('ENV')
if not ENV:
    raise Exception('Environment variable ENV is required!')

SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise Exception('Environment variable SECRET_KEY is required!')


# Add python paths
PROJECT_DIR = Path(__file__).resolve(strict=True).parent.parent
BASE_DIR = PROJECT_DIR.parent
sys.path.append(os.path.join(PROJECT_DIR, 'apps/'))


# URLs and runtime values
ROOT_URLCONF = 'myapp.urls'
WSGI_APPLICATION = 'myapp.wsgi.application'
# ASGI_APPLICATION = "myapp.asgi.application"
USE_X_FORWARDED_PORT = True
RUNTIME_VOLUME = '/data'


# Logging
LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'myapp': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        }
    },
}


# Application definition
ENV_APPS = []
PROJECT_APPS = ['account']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_extensions',
    'channels',
    'corsheaders',
    'storages',
    'django_countries',
    'django_filters',
    'social_django',
    'health_check',
    'health_check.db',
    'health_check.cache',
    'health_check.storage',
    'health_check.contrib.migrations',
    # 'health_check.contrib.celery',
    # 'health_check.contrib.celery_ping',
    'health_check.contrib.psutil',
    'health_check.contrib.redis',
    'graphene_django',
    'graphql_jwt.refresh_token.apps.RefreshTokenConfig',
] + ENV_APPS + PROJECT_APPS

ENV_MIDDLEWARE = []
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
] + ENV_MIDDLEWARE


# Templates
TEMPLATES_DIR = os.path.join(PROJECT_DIR, 'templates')
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# User & Account & Social Auth
AUTH_USER_MODEL = 'account.User'

PASSWORD_RESET_TIMEOUT_DAYS = 1
ACCOUNT_CREATION_TIMEOUT = 60 * 60 * 24 * 7
EMAIL_CHANGE_TIMEOUT = 60 * 60 * 24

SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL
SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it in a simple
    # format to create the user instance later. In some cases the details are
    # already part of the auth response from the provider, but sometimes this
    # could hit a provider API.
    'social_core.pipeline.social_auth.social_details',

    # Get the social uid from whichever service we're authing thru. The uid is
    # the unique identifier of the given user in the provider.
    'social_core.pipeline.social_auth.social_uid',

    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social_core.pipeline.social_auth.auth_allowed',

    # Checks if the current social-account is already associated in the site.
    'social_core.pipeline.social_auth.social_user',

    # Make up a username for this person, appends a random string at the end if
    # there's any collision.
    'social_core.pipeline.user.get_username',

    # Send a validation email to the user to verify its email address.
    # Disabled by default.
    # 'social_core.pipeline.mail.mail_validation',

    # Associates the current social details with another user account with
    # a similar email address. Disabled by default.
    # 'social_core.pipeline.social_auth.associate_by_email',

    # Create a user account if we haven't found one yet.
    'social_core.pipeline.user.create_user',

    # Create the record that associates the social account with the user.
    'social_core.pipeline.social_auth.associate_user',

    # Populate the extra_data field in the social record with the values
    # specified by settings (and the default ones like access_token, etc).
    'social_core.pipeline.social_auth.load_extra_data',

    # Update the user record with any changed info from the auth service.
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.open_id.OpenIdAuth',
    # 'social_core.backends.google.GoogleOpenId',
    # 'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.google.GoogleOAuth',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.yahoo.YahooOpenId',
    'graphql_jwt.backends.JSONWebTokenBackend',
    'django.contrib.auth.backends.ModelBackend',
)


# Fernet cryptography
FERNET_KEYS = []


# GraphQL
GRAPHENE = {
    # Set your schema
    "SCHEMA": "myapp.schema.schema",
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],
}

GRAPHQL_JWT = {
    'JWT_ALLOW_ARGUMENT': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_LONG_RUNNING_REFRESH_TOKEN': True,
    'JWT_EXPIRATION_DELTA': timedelta(minutes=30),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=7),
    'JWT_AUTH_HEADER_NAME': 'HTTP_APPAUTH',
}


# Storages
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', None)

# 1-week long s3 signed link expiration
AWS_QUERYSTRING_EXPIRE = 604800

# AWS S3 settings
if all([AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_STORAGE_BUCKET_NAME]):
    AWS_S3_REGION_NAME = os.environ.get('AWS_REGION_NAME', 'us-west-2')
    AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
    AWS_DEFAULT_ACL = 'private'

    DEFAULT_FILE_STORAGE = 'myapp.storages.MediaS3Storage'
    MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN

    INSTALLED_APPS += ['health_check.contrib.s3boto_storage', ]

# Sendgrid
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', None)

if SENDGRID_API_KEY:
    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"

MAX_UPLOAD_SIZE = 1024 * 1024 * 4000  # 4GB

# Billing?

# Monitoring?

# Cache
REDIS_URL = os.environ.get('REDIS_URL', "redis://redis:6379/1")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Celery?
