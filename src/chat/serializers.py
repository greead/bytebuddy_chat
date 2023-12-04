from rest_framework import serializers
from .models import Profile, IDE, ChatRoom

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        lookup_field = 'user_id'

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['name', 'online']
        
class IDESerializer(serializers.ModelSerializer):
    class Meta:
        model = IDE
        fields = ['code']
        lookup_field = 'chat_room_id'