import json
from django.contrib.auth.models import User
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from .models import *

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.chat_slug=self.scope['url_route']['kwargs']['room_slug']
        self.room_group_name='chat_%s' %self.chat_slug
        user=self.scope["user"]
        room = await self.get_room()  

        if room and user in await self.get_room_users(room): 
            await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
            )
            await self.accept()
        else:
            await self.send_json({"error": "You do not have access to this room."}) 
            await self.close()


    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    #triggered when   sending a message
    async def  receive(self,text_data):
        data =json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']

        #extranct the data that have been sent form the front end after sending a message to the group

        await self.save_message(username, room, message)
        #send the meassage to other users
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'room':room,
            }
        )
    #triggered when reciving a message
    async def chat_message(self,event):
        room = event['room']
        #send the messaage info to the front end
        latest_message=await self.get_latest_message(room)
        await self.send(text_data=json.dumps({
            'message': latest_message.content,
            'author': latest_message.author.username,
            'created_at': latest_message.created_at.strftime('%Y-%m-%d'),
        }))

    #asyncronize the function that create a message insranes
    @sync_to_async
    def save_message(self, username, room, message):

        user = User.objects.get(username=username)
        current_room = Room.objects.get(slug=room)
        Message.objects.create(author=user, room=current_room, content=message)

    @database_sync_to_async
    def get_room(self):
        try:
            return Room.objects.get(slug=self.chat_slug)
        except Room.DoesNotExist:
            return None

    @database_sync_to_async
    def get_room_users(self, room):
        return list(room.users.all())
    
    @database_sync_to_async
    def get_latest_message(self, room):
        return Message.objects.select_related('author').filter(room__slug=room).first()