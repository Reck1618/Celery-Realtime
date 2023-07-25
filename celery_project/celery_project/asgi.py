"""
ASGI config for celery_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from integers_app.routing import integers_urlpatterns
from chat_app.routing import chat_urlpatterns

ws_urlpatterns = integers_urlpatterns + chat_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_project.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
}) 
