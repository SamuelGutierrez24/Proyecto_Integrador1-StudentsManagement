from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Alerta

def menu(request):

    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if(noti.type==3):
            notifi.append(noti)
    
    notifi.reverse()    
    return render(request, 'menuBalanceAcademico.html', {'notificaciones': notifi})