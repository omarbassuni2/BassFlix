from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from newsfeed.views import display_movies
# Create your views here.
from accounts.forms import *


def login_view(request):
    context = {}
    user = request.user
    if request.user.is_authenticated:
        return redirect('display_movies')

    if request.POST:
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('display_movies')
    else:
        form = UserAuthenticationForm(request.POST)
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def register(request):
    form = CreateUserForm(request.POST)
    if form.is_valid():
        form.save()
        form = CreateUserForm()
        return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

