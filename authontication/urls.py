from django.urls import path
from django.contrib.auth.views import LoginView,logout_then_login
from . import views
urlpatterns = [
    path("login/",LoginView.as_view(template_name='authontication/Login.html'),name='login'),
    path("logout/",LoginView.as_view(),name='logout'),
    path("singup/",views.SigneUp,name='singup'),
    path("editprofile/",views.EditProfile,name='editprofile')
]