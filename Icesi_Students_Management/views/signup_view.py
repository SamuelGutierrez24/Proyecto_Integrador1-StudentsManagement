from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def signup(request):
    if request.method == 'POST':
        print("2")
        if (request.POST.get('username')
                and request.POST.get('email')
                and request.POST.get('password1')
                and request.POST.get('password2')):
            print("3")
            if request.POST['password1'] == request.POST['password2']:
                print("4")
                try:
                    user = User.objects.create_user(username=request.POST['username'],
                                                    password=request.POST['password1'])
                    user.save()
                    login(request, user)
                    return redirect('signin')
                except IntegrityError:
                    return render(request, 'signup.html', {
                        "error": 'Usuario ya existe'
                    })
            return render(request, 'signup.html', {
                "error": 'Contrasenas son distintas'
            })
        else:
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                "error": 'Todos los campos son requeridos'
            })
    else:
        print("1")
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
