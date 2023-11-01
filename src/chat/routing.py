from django.urls import re_path

from . import chatconsumer

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', chatconsumer.ChatConsumer.as_asgi()),
]