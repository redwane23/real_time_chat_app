from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
class Room(models.Model):
    GROUP = 'public'
    CHAT =  'privete'
    ROOM_TYPES=[ 
        (GROUP,'public group'),
        (CHAT,'privet chat')
    ]

    name=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    users=models.ManyToManyField(User,through='RoomUser',related_name='rooms')
    room_type=models.CharField(max_length=7,choices=ROOM_TYPES,default=GROUP)

    def room_size(self):
        return 15 if self.room_type == self.GROUP else 2

    def __str__(self) :
        return self.name


class Message(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.CharField(max_length=300)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    def __str__(self) :
        return f'{self.author} - {self.content[:10]}'


class Profile(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    username=models.CharField(max_length=300)
    profile_picture=models.ImageField(upload_to='profiles/',blank=True,null=True)
    bio=models.TextField()



class RoomUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if self.room.users.count() >= self.room.room_size():
            raise ValidationError(f"This {self.room.get_room_type_display()} is full.")
        else:
            return super().save( *args, **kwargs)
    
    class Meta:
        unique_together = ('user', 'room')
