from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def signup(request):
    print("1")
    if request.method == 'GET':
        print("2")
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        print("3")
        if request.POST['password1'] == request.POST['password2']:
            print("4")
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Contrasenas son distintas'
        })
