from django.shortcuts import render, redirect
from ..models import *

def menu(request):


    if request.method == 'GET':

        notificaciones = Alerta.objects.all()
        notifi = []
        history = HistoryActivityAssistance.objects.all()
        histo = []

        for noti in notificaciones:
            if(noti.type==2):
                notifi.append(noti)
        
        for histor in history:
            if(histor.activity.tipo==1):
                histo.append(histor)

        return render(request, 'menuBU.html', {'notificaciones': reversed(notifi), 'history': histo})
    
    else:

        id = request.POST["noti"]
        print(id)
        noti = Alerta.objects.all().filter(id =  id).first()

        return render(request, 'notification.html', {'noti': noti})


    