from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
import json

from .models import ChatRoom, Message, IDE

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

        # create/get room_name, create/get ide
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f'chat_{self.room_name}'
        self.room = ChatRoom.objects.get_or_create(name=self.room_name)[0]
        self.ide = IDE.objects.get_or_create(chat_room_id=self.room.id)
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

        # add user as online
        self.room.online.add(self.user)

        # send the user list to the newly joined user
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
            'type': 'user_list',
            'users': [user.username for user in self.room.online.all()],
            }
        )

        #send notification
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'user_join',
                'user': self.user.username,
                'message': f"{self.user.username} joined the chat"
            }
        )
        
        # send last 30 messages
        last_30 = [{'user':last.user.username,'content':last.content} for last in reversed(Message.objects.filter(room=self.room).order_by('-timestamp')[:30])]
        self.send(json.dumps(
            {
                'type': 'message_list',
                'user': self.user.username,
                'message': last_30
            }
        ))

    def close_during_connect(self, code):
        self.accept()
        self.close(code=code)


    def disconnect(self, close_code):
        '''
            Disconnect method used to close connection to web socket
        '''
        # log each disconnect
        print("ChatConsumer: disconnect")

        #send notification
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'user_leave',
                'user': self.user.username,
                'message': f"{self.user.username} has left the chat"
            }
        )

        # disconnect
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )
        self.room.online.remove(self.user)
    

    def receive(self, text_data=None, bytes_data=None):
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
    
    def user_join(self, event):
        '''
            Called when user joins chat room
        '''
        print("ChatConsumer: user_join")

        self.send(text_data=json.dumps(event))

    def user_list(self, event):
        '''
            Returns the current users online
        '''
        print("ChatConsumer: user_list")

        self.send(text_data=json.dumps(event))

    def message_list(self, event):
        '''
            Returns the last 30 messages to chat
        '''
        print("ChatConsumer: message_list")

        self.send(text_data=json.dumps(event))
    
    def user_leave(self, event):
        '''
            Returns the last 30 messages to chat
        '''
        print("ChatConsumer: message_list")

        self.send(text_data=json.dumps(event))