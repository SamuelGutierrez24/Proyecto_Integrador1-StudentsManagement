from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Alerta
from django.contrib.auth.decorators import user_passes_test, login_required

# def rol_check(user):
#     return user.rol == 2
#
#
# @login_required
# @user_passes_test(rol_check, "/signin/")

def menu(request):

    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if(noti.type==3):
            notifi.append(noti)
    
    notifi.reverse()    
    return render(request, 'menuBalanceAcademico.html', {'notificaciones': notifi})