from django.shortcuts import render, redirect
from ..models import *
from django.contrib.auth.decorators import user_passes_test, login_required



def rol_check(user):
    return user.rol == 6


@login_required
@user_passes_test(rol_check, "/signin/")
def CreaMenu(request):

    if request.method == 'GET':

        notificaciones = Alerta.objects.all()
        notifi = []
        history = HistoryActivityAssistance.objects.all()
        histo = []

        for noti in notificaciones:
            if(noti.type==5):
                notifi.append(noti)
        
        
        
        for histor in history:
            if(histor.activity.tipo==2):
                histo.append(histor)


        return render(request, 'menuCREA.html', {'notificaciones': reversed(notifi), 'history': histo} )
    
    else:

        id = request.POST["noti"]
        print(id)
        noti = Alerta.objects.all().filter(id =  id).first()

        return render(request, 'notification.html', {'noti': noti})


    