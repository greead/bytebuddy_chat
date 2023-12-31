from django.contrib.auth.models import User
from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=128)
    online = models.ManyToManyField(to=User, blank=True)
    created = models.TimeField(auto_now_add=True)
    lastUpdate = models.TimeField(auto_now=True)
    # ownerID = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_chatrooms")

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
    '''
        Model for all messages sent through the chat rooms
    '''
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    room = models.ForeignKey(to=ChatRoom, on_delete=models.CASCADE)
    content = models.CharField(max_length=512)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content} [{self.timestamp}]'

class Profile(models.Model):
    '''
        Model for all users profiles
    '''
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=16)
    bio = models.CharField(max_length=256)
    picture = models.ImageField(upload_to='images/', default='images/basicProfile.png', blank=True)


class IDE(models.Model):
    '''
        Model for synchronizing the IDE's in each chat room
    '''
    code = models.CharField(default='', max_length=1000)
    name = models.CharField(max_length=128 )