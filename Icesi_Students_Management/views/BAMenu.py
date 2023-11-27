from django.shortcuts import render, redirect, get_object_or_404
from Icesi_Students_Management.models import *
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse
from django.http import HttpResponse


def rol_check(user):
    return user.rol == 5


@login_required
@user_passes_test(rol_check, "/signin/")

def menu(request):
    estudiante = Student.objects.all()

    queryset = request.GET.get("buscar")
    if queryset:
        estudiante = Student.objects.filter(
            Q(code__icontains=queryset)
        ).distinct()
    
    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if (noti.type == 3):
            notifi.append(noti)
    notifi.reverse()

    if request.method == 'POST':
        codigo_estudiante = request.POST.get('inputBuscarEstud')

        # Buscar al estudiante por su nombre en la base de datos
        student = Student.objects.all().filter(code=codigo_estudiante).exists()
        
        if student == True:
            nombre = Student.objects.all().get(code=codigo_estudiante).name
            apellido = Student.objects.all().get(code=codigo_estudiante).lastName
            codigo = Student.objects.all().get(code=codigo_estudiante).code

            request.session['estudData'] = {'nombre': nombre, 'apellido': apellido, 'codigo': codigo}
            return redirect('registroNotasBA.html')

    return render(request, 'BalanceAcademicoCAMBIOS.html', {"estudiante": estudiante, 'notificaciones': notifi})
