from django.shortcuts import render, redirect, get_object_or_404
from Icesi_Students_Management.models import *
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test, login_required

# def rol_check(user):
#     return user.rol == 4
#
#
# @login_required
# @user_passes_test(rol_check, "/signin/")
def menuContabilidad(request):
    return render(request, 'menuContabilidad.html')   

def menu(request):
    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if (noti.type == 1):
            notifi.append(noti)
    notifi.reverse()
    return render(request, 'menuContabilidad.html', {'notificaciones': notifi})

def ver_noti(request, id):
    try:
        noti = Alerta.objects.get(id=id)
    except Alerta.DoesNotExist:
        raise Http404("Notificación no encontrada")

    return render(request, 'notificacion.html', {'noti': noti})

def eliminar_noti(request,id):
    notificacion = get_object_or_404(Alerta, id=id)
    notificacion.delete()
    return redirect('/contabilidad')
