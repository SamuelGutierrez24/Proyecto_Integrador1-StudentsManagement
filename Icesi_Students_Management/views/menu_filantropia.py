from django.shortcuts import render
from Icesi_Students_Management.models import Alerta

def menu(request):

    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if(noti.type==0):
            notifi.append(noti)

    return render(request, 'menu_filantropia.html', {'notificaciones': notifi})