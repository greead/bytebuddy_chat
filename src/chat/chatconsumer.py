from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from django.core.serializers import serialize
from django.utils import timezone
from django.core.paginator import Paginator

import json
import asyncio

class ChatConsumer(AsyncJsonWebsocketConsumer):
    '''
        Class to handle web socket connections from chat application
    '''

    async def connect(self):
        '''
            Connect method used for initial connections
        '''
        # log each connection for troubleshooting
        print("ChatConsumer: connect: " + str(self.scope["user"]))

        # allow connections
        await self.accept()


    async def disconnect(self):
        '''
            Disconnect method used to close connection to web socket
        '''
        # log each disconnect
        print("ChatConsumer: disconnect")

        await self.disconnect()
    

    async def receive_message(self, event):
        '''
            Called when someone has sent a message
        '''
        print("ChatConsumer: receive_message")

        await self.send_json(
            {
                "username": event['username'],
                "user_id": event['user_id'],
                "message": event['message']
            }
        )
    

    async def send_message(self, event):
        '''
            Called when sending a message to users
        '''
        print("ChatConsumer: send_message")

        await self.send_json(
            {
                "message": event['message']
            }
        )