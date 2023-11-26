from django.shortcuts import render, redirect, get_object_or_404
from Icesi_Students_Management.models import *
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from Icesi_Students_Management.models import *
from django.db.models import Q

# def rol_check(user):
#     return user.rol == 4
#
#
# @login_required
# @user_passes_test(rol_check, "/signin/")

def menuContabilidad(request):
    estudiante = Student.objects.all()

    queryset = request.GET.get("buscar")
    if queryset:
        estudiante = Student.objects.filter(
            Q(code__icontains=queryset)
        ).distinct()
    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if (noti.type == 1):
            notifi.append(noti)
    notifi.reverse()
    return render(request, 'menuContabilidad.html', {"estudiante": estudiante,'notificaciones': notifi})

def eliminar_estudiante(request, code):
    estudiante = get_object_or_404(Student, code=code)
    infoFinan = get_object_or_404(InformacionFinanciera, studentID=code)
    estudiante.delete()
    infoFinan.delete()
    return redirect('/contabilidad')

def ver_noti(request, id):
    try:
        noti = Alerta.objects.get(id=id)
    except Alerta.DoesNotExist:
        raise Http404("Notificación no encontrada")

    return render(request, 'notificacion.html', {'noti': noti})

def eliminar_noti(request,id):
    notificacion = get_object_or_404(Alerta, id=id)
    notificacion.delete()
    return redirect('/contabilidad')
