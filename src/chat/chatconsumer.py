from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
import json

from .models import ChatRoom, Message

class ChatConsumer(WebsocketConsumer):
    '''
        Class to handle web socket connections from chat application
    '''

    def connect(self):
        '''
            Connect method used for initial connections
        '''
        # log each connection for troubleshooting
        print("ChatConsumer: connect: " + str(self.scope["user"]))

        # get room_name
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f'chat_{self.room_name}'
        self.room = ChatRoom.objects.get_or_create(name=self.room_name)
        self.user = self.scope['user']

        if self.user.is_anonymous:
            self.close_during_connect(code=4401)
            return

        # allow connections
        self.accept()

        # join the room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

    def close_during_connect(self, code):
        self.accept()
        self.close(code=code)


    def disconnect(self, close_code):
        '''
            Disconnect method used to close connection to web socket
        '''
        # log each disconnect
        print("ChatConsumer: disconnect")

        # disconnect
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )
    

    def receive_message(self, text_data=None, bytes_data=None):
        '''
            Called when someone has sent a message
        '''
        print("ChatConsumer: receive_message")

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if not self.user.is_authenticated:
            return

        # send chat message event to the room
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user': self.user.username,
                'message': message,
            }
        )
        Message.objects.create(user=self.user, room=self.room, content=message)
    

    def chat_message(self, event):
        '''
            Called when sending a message to chat room
        '''
        print("ChatConsumer: send_message")

        self.send(text_data=json.dumps(event))