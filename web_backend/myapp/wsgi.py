"""
WSGI config for myapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

ENV = os.getenv('ENV')
if not ENV:
    raise Exception('Environment variable ENV is required!')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'myapp.settings.{ENV}')

application = get_wsgi_application()
