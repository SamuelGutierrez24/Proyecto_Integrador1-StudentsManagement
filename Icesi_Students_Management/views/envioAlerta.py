from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Alerta
from ..forms import envioMensaje
from django.contrib import messages

def enviarMensaje(request):
    if request.method == 'POST':
        form = envioMensaje(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"El mensaje ha sido enviado!")
            return redirect('menu filantropia')
    else:
        form = envioMensaje()

    return render(request, 'envioAlerta.html', {'form': form})