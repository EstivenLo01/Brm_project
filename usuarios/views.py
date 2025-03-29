from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # Asegúrate de que 'home' esté en tus URLs

        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("login")  # Asegúrate de que 'login' esté en tus URLs

@login_required  # Asegura que solo usuarios autenticados accedan
def home(request):
    return render(request, 'home.html')
