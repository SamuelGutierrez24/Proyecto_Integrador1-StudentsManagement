from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def signin(request):
    if request.method == "GET":
        return render(request, 'signin.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'error': 'Usuario y/o contrasena incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')

