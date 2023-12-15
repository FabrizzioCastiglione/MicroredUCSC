"""
ASGI config for microreducsc project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

import django
django.setup()



from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from channels.routing import URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from graph.routing import ws_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microreducsc.settings')

application = ProtocolTypeRouter({
  'http' : get_asgi_application(),
  'websocket': AllowedHostsOriginValidator(AuthMiddlewareStack(URLRouter(ws_urlpatterns))),
})

