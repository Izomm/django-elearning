"""
ASGI config for educa project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

from chat.routing import websocket_urlpatterns

from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educa.settings')


application = get_asgi_application()

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
'http': django_asgi_app,
'websocket': AuthMiddlewareStack(
URLRouter(websocket_urlpatterns)
),
})