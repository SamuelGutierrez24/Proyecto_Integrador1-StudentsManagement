from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from Icesi_Students_Management.models import *
from django.db.models import Q

def menuBuscar(request):
    estudiante = Student.objects.all()
    
    queryset = request.GET.get("buscar")
    if queryset:
        estudiante = Student.objects.filter(
            Q(code__icontains = queryset)
        ).distinct()
    return render(request, 'buscarEstud.html',{"estudiante":estudiante})

def eliminar_estudiante(request,code):
    estudiante = get_object_or_404(Student, code=code)
    infoFinan = get_object_or_404(InformacionFinanciera, studentID=code)
    estudiante.delete()
    infoFinan.delete()
    return redirect('/contabilidad/buscarEstud.html')
