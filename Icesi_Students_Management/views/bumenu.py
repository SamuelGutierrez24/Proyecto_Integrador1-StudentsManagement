from django.shortcuts import render, redirect

def home2(request):
    return render(request, 'home.html')