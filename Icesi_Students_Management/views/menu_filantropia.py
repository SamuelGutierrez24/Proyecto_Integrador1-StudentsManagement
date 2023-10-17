from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Alerta
from ..forms import envioMensaje

def menu(request):

    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if(noti.type==4):
            notifi.append(noti)

    return render(request, 'menu_filantropia.html', {'notificaciones': notifi})



