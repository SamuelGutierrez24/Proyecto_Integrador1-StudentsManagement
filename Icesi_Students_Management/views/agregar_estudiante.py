from django.shortcuts import render
from Icesi_Students_Management.models import Donante

def agregar(request):
    donadores = Donante.objects.all()
    return render(request, 'agregar_estudiante.html', {'donadores': donadores})