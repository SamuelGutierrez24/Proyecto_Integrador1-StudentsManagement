from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Donante
from Icesi_Students_Management.forms import *


def agregar(request):

    becas = Becas.objects.all()

    if request.method == 'POST':
        selected_button = request.POST.get('selected_button')
        request.session['boton_seleccionado'] = int(selected_button)
        return redirect('agregar estudiante')
    

    boton_seleccionado = request.session.get('boton_seleccionado', None)
    return render(request, 'agregar_estudiante.html', {'form': addStudent, 'Becas': becas, 'boton_seleccionado': boton_seleccionado})