from .dev import *

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

if SENDGRID_API_KEY:
    EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
    SENDGRID_SANDBOX_MODE_IN_DEBUG = True
    SENDGRID_ECHO_TO_STDOUT = True
    DEFAULT_FROM_EMAIL = 'Admin <noreply@test.example.com>'
