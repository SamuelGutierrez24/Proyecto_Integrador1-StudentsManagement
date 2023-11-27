from django.shortcuts import render, redirect
from django.http import HttpResponse
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Actividad
from Icesi_Students_Management.models import AsistenciaCREA
from Icesi_Students_Management.models import SeguimientoBeca
from Icesi_Students_Management.models import Alerta
from Icesi_Students_Management.models import HistoryActivityAssistance
from Icesi_Students_Management.forms import CreaForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 6


@login_required
@user_passes_test(rol_check, "/signin/")
def registerC(request):
    if request.method == 'GET':
        notificaciones = Alerta.objects.all()
        notifi = []

        for noti in notificaciones:
            if(noti.type==5):
                notifi.append(noti)

        return render(request, 'registroCREA.html',{
                'form': CreaForm,
                "studentInfo": "",
                'notificaciones': reversed(notifi)
         })
    else:
        if verifyItem(request.POST['student']):
            action = request.POST.get('action')
            studentCode = request.POST['student']
            if(action == 'search'):
                return getSession(studentCode,request)
            else:
                student = Student.objects.all().get(code=studentCode)
                followUp = SeguimientoBeca.objects.all().filter(studentID = student).first()
                activity = Actividad.objects.all().get(id=request.POST['activity'])
                reason = request.POST['reason']
                assistance = AsistenciaCREA.objects.create( activity= activity, seguimiento= followUp, reason = reason)
                assistance.save()
                history = HistoryActivityAssistance.objects.create(student=student,activity=activity)
                history.save()
                form = CreaForm(initial={'student': studentCode})
                if('Chk' in request.POST):
                    print('Si esta')
                    return render(request, 'registroCREA.html',{
                    'form': form,
                    "studentInfo": "true",
                    "nombre": student.name,
                    "apellido": student.lastName
                    })
                else:
                    print('No esta')
                    alert = Alerta.objects.create(title = 'Registro Actividad', type = 4, description = 'Se actualizaron las actividades del CREA del estudiante' + request.POST['student'], StudentID = Student.objects.all().get(code = studentCode))
                    alert.save()
                    return render(request, 'registroCREA.html',{
                    'form': CreaForm,
                    "alert":True,
                    "studentInfo": ""
                    })
        else:
            return render(request, 'registroCREA.html',{
                'form': CreaForm,
                "studentInfo": "",
                "error": 'El estudiante no existe'
             })


def verifyItem(item):
    return Student.objects.all().filter(code=item).exists()

def getSession(student,request):
    student = Student.objects.all().get(code=student)
    #actividad = Actividad.objects.all().get(id=activity)
    form = CreaForm(initial={'student': student})
    return render(request, 'registroCREA.html',{
        'form': form,
        "studentInfo": "true",
        "nombre": student.name,
        "apellido": student.lastName
        })

