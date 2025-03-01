import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Message.settings")
django.setup()

from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from home.routing import websocket_urlpatterns



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns),
    )
})