from django.urls import path
from . import views

urlpatterns=[
    path('<slug:slug>/',views.room),
    path('', views.room, {'slug': ''},name='home'),
]