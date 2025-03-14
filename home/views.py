from django.shortcuts import render,get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def room(request,slug):
    user= request.user
    if slug!='':
        rooms=user.rooms.all()
        room=get_object_or_404(rooms,slug=slug)
    else:
        rooms=user.rooms.all()
        room=[]
    context={
        'rooms':rooms,
        'room':room,
    }
    return render(request,"home/rooms.html",{'context':context})
