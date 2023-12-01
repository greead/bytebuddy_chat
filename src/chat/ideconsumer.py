from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
import json

from .models import ChatRoom, IDE

class IDEConsumer(WebsocketConsumer):
    '''
        Class to handle web socket connections from chat application
    '''
    def connect(self):
        
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"ide_{self.room_name}"
        self.ide = IDE.objects.get_or_create(name=self.room_name)[0]

        if self.ide:
            #allow connections
            self.accept()

            # join the room group
            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name,
            )

    
    def disconnect(self, code):
        '''
            Disconnect from ide consumer
        '''
        print("IDEConsumer: disconnect")

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )
    
    def receive(self, text_data=None, bytes_data=None):
        '''
            sync ide code with others in chat room
        '''
        print("IDEConsumer: receive_message")

        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'ide_message',
                'message': message
            }
        )
    
    def ide_message(self, event):
        '''
            Called when sending code changes to chatroom
        '''
        print("IDEConsumer: ide_message")

        self.send(text_data=json.dumps(event))