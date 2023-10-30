from django.shortcuts import render, redirect
from ..models import *

def CreaMenu(request):


    if request.method == 'GET':

        notificaciones = Alerta.objects.all()
        notifi = []

        for noti in notificaciones:
            if(noti.type==5):
                notifi.append(noti)

        return render(request, 'menuCREA.html', {'notificaciones': notifi})
    
    else:

        id = request.POST["noti"]
        print(id)
        noti = Alerta.objects.all().filter(id =  id).first()

        return render(request, 'notification.html', {'noti': noti})


    