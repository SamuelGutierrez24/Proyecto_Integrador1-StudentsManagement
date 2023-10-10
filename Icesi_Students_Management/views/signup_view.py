from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from Icesi_Students_Management.models import User
from django.contrib.auth import login
from django.db import IntegrityError


def signup(request):
    if request.method == 'POST':
        if (request.POST.get('name')
                and request.POST.get('lastName')
                and request.POST.get('username')
                and request.POST.get('email')
                and request.POST.get('phoneNumber')
                and request.POST.get('password1')
                and request.POST.get('password2')):
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.create_user(first_name=request.POST['name'], password=request.POST['password1'],
                                                    email=request.POST['email'], is_active=False, is_staff=False,
                                                    is_superuser=False, phone=request.POST['phoneNumber'],
                                                    last_name=request.POST['lastName'], username=request.POST['username'])
                    user.save()
                    login(request, user)
                    messages.success(request, 'Cuenta creada satisfactoriamente! (espera a que sea activada)')
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
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
