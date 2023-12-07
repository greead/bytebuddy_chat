from django.urls import re_path

from . import chatconsumer, ideconsumer

websocket_urlpatterns = [
    # path for chat websocket
    re_path(r'ws/chat/(?P<room_name>\w+)/$', chatconsumer.ChatConsumer.as_asgi()),
    # path for ide websocket
    re_path(r'ws/ide/(?P<room_name>\w+)/$', ideconsumer.IDEConsumer.as_asgi()),
]