from django.shortcuts import render, redirect
from ..forms import registrarInfoFinanciera
from ..models import InformacionFinanciera

def infoFinanciera(request):
    if request.method == 'GET':
        return render(request, 'infoFinanciera.html', {
            'form': registrarInfoFinanciera
        })
    else:
        InformacionFinanciera.objects.create(studentName=request.POST['studentName'],
                                             studentID=request.POST['studentID'],
                                             dineroAsignado=request.POST['dineroAsignado'],
                                             dineroUsado=request.POST['dineroUsado'],
                                             financialNote=request.POST['financialNote'],
                                             extraInfo=request.POST['extraInfo'])

        return redirect('/contabilidad/')
