from rest_framework import serializers
from .models import Profile, IDE, ChatRoom

class ProfileSerializer(serializers.ModelSerializer):
    '''
        Serializer for parsing a user profile
    '''
    class Meta:
        model = Profile
        fields = '__all__'
        lookup_field = 'user_id'

class ChatRoomSerializer(serializers.ModelSerializer):
    '''
        Serializer for parsing a chat room
    '''
    class Meta:
        model = ChatRoom
        fields = ['name', 'online']
        
class IDESerializer(serializers.ModelSerializer):
    '''
        Serializer for parsing an IDE
    '''
    class Meta:
        model = IDE
        fields = ['code']
        lookup_field = 'chat_room_id'