from django.shortcuts import render, redirect, get_object_or_404
from Icesi_Students_Management.models import *
from django.db.models import Q
from django.http import Http404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from Icesi_Students_Management.models import *
from django.db.models import Q

def menuTestimony(request):
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
    return render(request, 'testimonio.html', {"estudiante": estudiante,'notificaciones': notifi})