from django.shortcuts import render
from Icesi_Students_Management.models import Alerta
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from Icesi_Students_Management.models import Alerta
from ..forms import envioMensaje
from ..forms import modificarAlerta
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages


def rol_check(user):
    return user.rol == 2


@login_required
@user_passes_test(rol_check, "/signin/")
def enviarMensaje(request):
    if request.method == 'POST':
        form = envioMensaje(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El mensaje ha sido enviado!")
            return redirect('menu filantropia')
    else:
        form = envioMensaje()

    return render(request, 'envioAlerta.html', {'form': form})


def testimonio(request):
    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if (noti.type == 4):
            notifi.append(noti)

    return render(request, 'testimonio.html', {
        'notificaciones': notifi
    })


def menu(request):
    if request.method == 'GET':
        form = envioMensaje(request.POST)
        notificaciones = Alerta.objects.all()
        notifi = []

        for noti in notificaciones:
            if (noti.type == 4):
                notifi.append(noti)
                notifi.reverse()
        return render(request, 'menu_filantropia.html', {'notificaciones': notifi, 'form': form})
    else:
        form = envioMensaje(request.POST)
        notificaciones = Alerta.objects.all()
        notifi = []

        for noti in notificaciones:
            if (noti.type == 4):
                notifi.append(noti)
        if form.is_valid():
            form.save()
            messages.success(request, "El mensaje ha sido enviado!")
            return redirect('menu filantropia')
        id = request.POST["noti"]

        return redirect(reverse('envioAlerta', kwargs={'noti_id': id}))
