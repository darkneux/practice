import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels_redis.core import RedisChannelLayer
from channels.layers import get_channel_layer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practice.settings')
django.setup()

from channels.auth import AuthMiddlewareStack
from websocket.routing import websocket_urlpatterns


websocket_routing = URLRouter(
       websocket_urlpatterns
)


application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        websocket_routing
    )

})



