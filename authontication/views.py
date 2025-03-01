from django.shortcuts import render,redirect
from django.contrib.auth import login
from .forms import SignUpForm


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