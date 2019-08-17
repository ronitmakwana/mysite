from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
def home(request):
    count=User.objects.count()
    return render(request,'home.html',{'count':count})

def about(request):
    return render(request,'about.html',{})

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/doctor/home')
    else:
        form=UserCreationForm()
    return render(request,'registration/signup.html',{'form':form})

def user_profile(request):
    return render(request,'user_profile.html',{})