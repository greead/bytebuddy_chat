from django.contrib.auth.models import User
from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=User, blank=True)
    
    #chatRoomId = models.PositiveIntegerField()
    #roomName = models.CharField(max_length=255) 
    #description = models.TextField(max_length=200, blank=True, null=True)
    #replitLink = models.URLField()
    #isPublic =  models.BooleanField(default=False)
    #created = models.TimeField()
    #lastUpdate = models.TimeField()
    #ownerID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_chatrooms") 
    #memberID = models.ManyToManyField(User,related_name="chatrooms")
    

    def get_online_count(self):
        return self.online.count()

    def join(self, user):
        self.online.add(user)
        self.save()

    def leave(self, user):
        self.online.remove(user)
        self.save()

    def __str__(self):
        return f'{self.name} ({self.get_online_count()})'


class Message(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'

class Profile(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=16)
    bio = models.CharField(max_length=256)
    picture = models.ImageField(upload_to='images/', blank=True)
