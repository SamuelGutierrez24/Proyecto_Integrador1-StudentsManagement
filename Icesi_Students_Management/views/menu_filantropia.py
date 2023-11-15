from django.shortcuts import render
from Icesi_Students_Management.models import Alerta
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from Icesi_Students_Management.models import Alerta
from ..forms import envioMensaje
from ..forms import modificarAlerta
from django.contrib.auth.decorators import user_passes_test, login_required

# def rol_check(user):
#     return user.rol == 2
#
#
# @login_required
# @user_passes_test(rol_check, "/signin/")
def menu(request):
    if request.method == 'GET':
        
        notificaciones = Alerta.objects.all()
        notifi = []

        for noti in notificaciones:
            if(noti.type==4):
                notifi.append(noti)

        return render(request, 'menu_filantropia.html', {'notificaciones': notifi})
    else:
        
        id = request.POST["noti"]
        print(id)

        return redirect(reverse('envioAlerta', kwargs={'noti_id': id}))
