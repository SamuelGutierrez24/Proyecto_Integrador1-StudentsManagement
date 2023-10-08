from django.shortcuts import render, redirect
from Icesi_Students_Management.models import *
from django.db.models import Q

def menuContabilidad(request):
    return render(request, 'menuContabilidad.html')   

def menu(request):
    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if (noti.type == 0):
            notifi.append(noti)

    return render(request, 'menuContabilidad.html', {'notificaciones': notifi})
