"""
ASGI config for myapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

ENV = os.getenv('ENV')
if not ENV:
    raise Exception('Environment variable ENV is required!')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'myapp.settings.{ENV}')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
})
