from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Alerta
from ..forms import envioMensaje
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 2


@login_required
@user_passes_test(rol_check, "/signin/")
def enviarMensaje(request):
    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if(noti.type==4):
            notifi.append(noti)
    if request.method == 'POST':
        form = envioMensaje(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"El mensaje ha sido enviado!")
            return redirect('menu filantropia')
    else:
        form = envioMensaje()

    return render(request, 'envioAlerta.html', {'form': form,'notificaciones': notifi})