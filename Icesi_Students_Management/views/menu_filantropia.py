from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Alerta
from ..forms import envioMensaje

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
        noti = Alerta.objects.all().filter(id =  id).first()

        return render(request, 'notificacionEditable.html', {'noti': noti})



