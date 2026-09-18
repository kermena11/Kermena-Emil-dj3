from django.shortcuts import render

def home(request):
    return render(request,'trainee/home.html')

def profile(request):
    return render(request,'trainee/profile.html')
