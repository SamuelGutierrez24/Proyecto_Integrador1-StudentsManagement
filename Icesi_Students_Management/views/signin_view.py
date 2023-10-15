from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def signin(request):
    if request.method == "GET":
        print("Sapa")
        return render(request, 'signin.html')
    else:
        print(request.POST)
        print('malparido')
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        print(user.rol)
        if user is None
            return render(request, 'signin.html', {
                'error': 'Usuario y/o contrasena incorrecta'
            })
        else:
            if(user.rol == 3 ):
                login(request, user)
                return redirect('bienestarUniversitario')    
            
            else:
                if user.rol == 0:
                    login(request, user)
                    return redirect('home')
