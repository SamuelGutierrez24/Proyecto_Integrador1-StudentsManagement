from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Becas
from Icesi_Students_Management.forms import modificarAlerta

def modificar(request):

    if request.method == 'POST':
        form = modificarAlerta(request.POST)

    return render(request, 'notificacionEditable.html', {'form': form})
