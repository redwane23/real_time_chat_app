from django.urls import path
from . import views

urlpatterns = [

    path("get_paginated_messages/<str:room_slug>/",views.get_paginated_messages.as_view()),
    path("get_messages/<str:room_slug>/",views.get_messages.as_view()),
    path('get_room/<str:search_term>/',views.RoomUsersSearch),
    path('join_room/<str:RoomName>/',views.JoinRoom),

]