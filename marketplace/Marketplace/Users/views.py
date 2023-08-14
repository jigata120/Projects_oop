from django.shortcuts import render, redirect,  get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from Market.models import Cart

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        user = User.objects.create_user(username=username, password=password, email=email,)
        user.save()
        cart = Cart.objects.create(buyer=user)
        cart.save()

        return redirect('login')
    else:
        return render(request, 'Usertemplate/Users/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'Usertemplate/Users/login.html')
    else:
        return render(request, 'Usertemplate/Users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')
