from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignUpForm,ProfileEditForm
from django.contrib.auth.decorators import login_required
from home.models import Profile



def SigneUp(request):
    if request.method =='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request,user)
            return redirect("home")
    else:
        form=SignUpForm()
        return render(request,'authontication/SignUp.html',{'form':form})

@login_required
def EditProfile(request):
    profile=Profile.objects.get(owner=request.user)
    if request.method=='POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=ProfileEditForm()
        return render(request,'authontication/EditProfile.html',{'form':form})