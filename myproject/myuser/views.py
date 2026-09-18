from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

def login(request):
    if request.user.is_authenticated:
        return redirect("alltracks")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect("alltracks")
        messages.error(request, "Invalid username or password.")
    return render(request, "myuser/login.html")

def signup(request):
    if request.user.is_authenticated:
        return redirect("alltracks")
    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        if not username or not password:
            messages.error(request, "Username and password are required.")
        elif password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        else:
            User.objects.create_user(username=username, password=password)
            return redirect("login")
    return render(request, "myuser/signup.html")

def logout(request):
    if request.method == "POST":
        auth_logout(request)
        return redirect("login")
    return render(request, "myuser/logout.html")
