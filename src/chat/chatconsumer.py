from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from channels.db import database_sync_to_async
import json

from .models import ChatRoom, Message, IDE, Profile

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
        self.user = self.scope['user']
        self.display_name = Profile.objects.filter(user=self.user)[0].display_name

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

        # send active users and their profile pics
        active_users_and_images = []
        for user in self.room.online.all():
             print("USER", user)
             qs = Profile.objects.filter(user=user)             
             print("QS", qs)
             if qs.exists():
                active_users_and_images.append({"user":qs[0].display_name, "image": qs[0].picture.url})
                print("PROFILE", {"user":qs[0].display_name, "image": qs[0].picture.url})
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
            'type': 'user_list',
            'message': active_users_and_images,
            }
        )

        #send notification
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'user_join',
                'user': self.display_name,
                'message': f"{self.display_name} joined the chat"
            }
        )
        
        # send last 30 messages
        last_30_messages = []
        messages = Message.objects.filter(room=self.room).order_by('-timestamp')[:30]
        for message in reversed(messages):
            user_profile = Profile.objects.filter(user=message.user)
            if user_profile.exists():
                last_30_messages.append({'user': user_profile[0].display_name, 'content': message.content})
            else:
                last_30_messages.append({'user': message.user.username, 'content': message.content})
        self.send(json.dumps(
            {
                'type': 'message_list',
                'user': self.display_name,
                'message': last_30_messages
            }
        ))

    def close_during_connect(self, code):
        '''
            Close websocket with specific code
        '''
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
                'user': self.display_name,
                'message': f"{self.display_name} has left the chat"
            }
        )

        # disconnect
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name,
        )

        #remove user from online
        self.room.online.remove(self.user)

        # send the updated user list
        active_users_and_images = []
        for user in self.room.online.all():
             qs = Profile.objects.filter(user=user)
             if qs.exists():
                active_users_and_images.append({"user":qs[0].display_name, "image": qs[0].picture.url})
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
            'type': 'user_list',
            'message': active_users_and_images,
            }
        )
    

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
                'user': self.display_name,
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