from django.shortcuts import render
from Icesi_Students_Management.models import Donante
from Icesi_Students_Management.forms import *

def agregar(request):
    if request.method == 'GET':
        print('enviando formulario')
        #Investigar como confirmar que los campos se encuentren llenos para guardar la informacion
        #Averiguar porque hay un error a la hora de incluir el forms para seleccionar donador
        return render(request, 'agregar_estudiante.html',{'form': addStudent})