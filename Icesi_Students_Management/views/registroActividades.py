from django.shortcuts import render, redirect
from Icesi_Students_Management.forms import ActivityForm

def registroA(request):
    return render(request, 'registroActividad.html',{
        'form': ActivityForm
    })