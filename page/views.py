from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, "User doesn't exists.")
            return redirect("/login/")
        
        user = authenticate(username = username,password = password)
        if user is None:
            messages.error(request,"Invalid Password")
        else:
            login(request, user)
            messages.info(request, "Login Successful")
            return redirect("/")
        
    if request.user.is_authenticated:
        messages.info(request, "Logout Successful.")
        return redirect("/logout/")
    
    return render(request,"login.html")


def logout_page(request):
    logout(request)
    messages.info(request, "Logout Successful.")
    return redirect("/login/")



def register(request):
    if request.method =="POST":
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email =data.get('email')
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.error(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            )
        
        user.set_password(password)
        user.save()
        messages.info(request, "Successfully created an account.")
        return redirect('/register/')
    
    
    if request.user.is_authenticated:
        messages.info(request,"Logout Successful.")
        return redirect("/register/")
    
    return render(request, "register.html")


@login_required(login_url="/login/")
def Home(request):

    return render(request,"index.html")