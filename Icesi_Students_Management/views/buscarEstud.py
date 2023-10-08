from django.shortcuts import render, redirect
from Icesi_Students_Management.models import *
from django.db.models import Q

def menuBuscar(request):
    infoFinan = InformacionFinanciera.objects.all()
    queryset = request.GET.get("buscar")
    if queryset:
        infoFinan = InformacionFinanciera.objects.filter(
            Q(studentID__icontains = queryset)
        ).distinct()
    return render(request, 'buscarEstud.html',{"infoFinan":infoFinan})