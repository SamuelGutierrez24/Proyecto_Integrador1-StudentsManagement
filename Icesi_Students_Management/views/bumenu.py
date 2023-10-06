from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Alerta

def menu(request):


    if request.method == 'GET':

        notificaciones = Alerta.objects.all()
        notifi = []

        for noti in notificaciones:
            if(noti.type==0):
                notifi.append(noti)
        


    return render(request, 'menuBU.html', {'notificaciones': notifi})