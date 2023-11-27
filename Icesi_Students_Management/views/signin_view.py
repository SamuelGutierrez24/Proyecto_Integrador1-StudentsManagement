from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def signin(request):
    logout(request)
    if request.method == "GET":
        return render(request, 'signin.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.rol == 2:
                login(request, user)
                return redirect('menu filantropia')
            elif user.rol == 3:
                login(request, user)
                return redirect('bienestarUniversitario')
            elif user.rol == 4:
                login(request, user)
                return redirect('menuContabilidad')
            elif user.rol == 5:
                login(request, user)
                return redirect('menuBalanceAcademico')
            elif user.rol == 6:
                login(request, user)
                return redirect('crea')
            elif user.rol == 0:
                messages.error(request, "No puede ingresar. Su usuario no tiene un rol asignado")
                return render(request, 'signin.html')
            else:
                messages.error(request, "Rol de usuario no valido")
                return render(request, 'signin.html')
        else:
            messages.error(request, "Usuario y/o contrasena incorrecta")
            return render(request, 'signin.html')
