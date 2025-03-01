from rest_framework import serializers
from home.models import Message,Room
from django.contrib.auth.models import User

class MessageSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    created_at = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = ['content', 'author','created_at']
    def get_created_at(self, obj):
        return obj.created_at.date()

class Roomserializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields=['name'] 

class Userserializer(serializers.ModelSerializer):
    is_friend = serializers.SerializerMethodField('get_is_friend') 
    class Meta:
        model = User
        fields = ['id', 'username', 'is_friend']  

    def get_is_friend(self, obj):
        request_user = self.context.get("request").user  
        return Room.objects.filter(room_type='privete').filter(users=obj).filter(users=request_user).exists()
