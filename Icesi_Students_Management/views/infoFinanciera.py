from django.shortcuts import render, redirect
from ..forms import registrarInfoFinanciera
from ..models import InformacionFinanciera, Student, SeguimientoBeca
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 4


@login_required
@user_passes_test(rol_check, "/signin/")
def infoFinanciera(request):
    if request.method == 'POST':
        student_id = request.POST['studentID']

        if Student.objects.filter(code=student_id).exists():
            if InformacionFinanciera.objects.filter(studentID=student_id).exists():
                messages.error(request, 'El estudiante ya tiene Información Financiera Registrada')
            else:
                estudiante = Student.objects.get(code=student_id)
                seguimiento_beca = SeguimientoBeca.objects.get(
                    studentID=estudiante)
                beca = estudiante.beca.type

                gastoTotal = 0
                dineroTransporte = 0
                dineroAlimentacion = 0
                dineroMatricula = (estudiante.beca.percentage / 100) * float(seguimiento_beca.carreraID.precioMatricula)

                dineroTotal = dineroMatricula

                if estudiante.beca.alimentacion == True:
                    dineroTotal = dineroTotal + 800000
                    dineroAlimentacion = dineroAlimentacion + 800000

                if estudiante.beca.transporte == True:
                    dineroTotal = dineroTotal + 432000
                    dineroTransporte = dineroTransporte + 432000

                InformacionFinanciera.objects.create(studentID=student_id,
                                                     type=beca,
                                                     dineroAsignado=dineroTotal,
                                                     matriculaBeca=dineroMatricula,
                                                     transporteBeca=dineroTransporte,
                                                     alimentacionBeca=dineroAlimentacion,
                                                     gasto=gastoTotal,
                                                     fecha=request.POST['fecha'],
                                                     seguimientoBecaID=seguimiento_beca)
                messages.success(request, 'Información Financiera registrada correctamente!')
        else:
            messages.error(request, 'El código del estudiante no existe.')
    return render(request, 'infoFinanciera.html', {
        'form': registrarInfoFinanciera
    })
