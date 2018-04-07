from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserCreationForm, AuthenticationForm

# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    #after user entered their details, that is a post request and user  is redirected to events homepage via this view(this generally happends after get)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('events:index')
    #if user has to enter thier detials, that would be get request, render the signup template for them to enter details
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    #same as signup
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('events:index')
    else:
        form = AuthenticationForm(request.POST)
    return render(request, 'accounts/signin.html', {'form':form})

def signout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('accounts:index')
