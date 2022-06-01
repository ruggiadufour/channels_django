from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.conf.urls import url
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'^ws/noti/(?P<room_name>\w+)$', consumers.NotificationConsumer),
]