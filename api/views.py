from home.models import Room,Message
from django.contrib.auth.models import User
from django.http import JsonResponse
from .serializers import MessageSerializer,Roomserializer,Userserializer
from .filters import RoomsFilter,UsersFilter
from django.contrib.auth.decorators import login_required
import json
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class get_paginated_messages(APIView):
    permission_classes = [IsAuthenticated]  
    def get(self,request,room_slug):
        paginator = PageNumberPagination()

        try:
            room = Room.objects.get(slug=room_slug)
            messages = Message.objects.filter(room=room).select_related('author')
            result_page = paginator.paginate_queryset(messages, request)
            serialized_data = MessageSerializer(result_page, many=True).data

            return paginator.get_paginated_response({
                'messages': serialized_data
            })

        except Room.DoesNotExist:
            return Response({'error': 'Room not found'}, status=404)

      
class get_messages(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,room_slug):

        try:
            room = Room.objects.get(slug=room_slug)
            messages = Message.objects.filter(room=room).select_related('author').first()
            serialized_data = MessageSerializer(messages).data
            data={
                'message': serialized_data     
            }
            return Response(data)
        except Room.DoesNotExist:
            return Response({'error': 'Room not found'}, status=404)  


@login_required
def RoomUsersSearch(request,search_term):
    excluded_rooms=Room.objects.exclude(users=request.user)
    exluded_users=User.objects.exclude(id=request.user.id)
    filtered_users=UsersFilter({'search':search_term},queryset=exluded_users)
    filtered_rooms=RoomsFilter({'search':search_term},queryset=excluded_rooms)

    serialized_rooms=Roomserializer(filtered_rooms.qs,many=True)
    serialized_users = Userserializer(filtered_users.qs, many=True, context={"request": request})
    rooms=serialized_rooms.data
    users=serialized_users.data
    data={
        'rooms':rooms,
        'users':users,
        }
    return JsonResponse(data,safe=False)

@login_required
def JoinRoom(request,RoomName):
    if request.method =='POST':
        try:
            data = json.loads(request.body)
            user=request.user  
            action = data.get("action")
            if action=='join':
                room=Room.objects.get(slug=RoomName)
                room.users.add(user)
            elif action=='leave':
                room=Room.objects.get(slug=RoomName)
                if(room.room_type=='privete'):
                    room.delet()
                room.users.remove(user)
            elif action=='create':

                second_user=User.objects.get(username=RoomName)
                new_room=Room(name=f'{request.user.username}/{second_user.username}',slug=f'{request.user.username}_{second_user.username}')
                new_room.save()
                new_room.users.add(user)
                new_room.users.add(second_user)
                new_room.save()


            return JsonResponse({'message':'added sucsufully'})

        except Room.DoesNotExist:
            return JsonResponse({'message':"an error accure cant add user"})


