from django.shortcuts import render, redirect
from django.http import HttpResponse
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Actividad
from Icesi_Students_Management.models import HistoryActivityAssistance
from Icesi_Students_Management.models import AsistenciasActividad
from Icesi_Students_Management.models import SeguimientoBeca
from Icesi_Students_Management.models import Alerta
from Icesi_Students_Management.models import User
from Icesi_Students_Management.forms import ActivityForm

def registroA(request):
    notificaciones = Alerta.objects.all()
    notifi = []
    for noti in notificaciones:
        if(noti.type==2):
            notifi.append(noti)
    notifi.reverse() 
    
    if request.method == 'GET':
        print('enviando formulario')
        return render(request, 'registroActividad.html',{
                'form': ActivityForm,
                "studentInfo": "",
                'notificaciones': notifi
                })
    else:
        studentToVerify = request.POST['student']
        studentInDB = Student.objects.all().filter(code=studentToVerify).exists()
        print(studentInDB)
        if studentInDB == False:
             return  render(request, 'registroActividad.html',{
                'form': ActivityForm,
                "studentInfo": "",
                "error": 'El estudiante no existe',
                'notificaciones': notifi
                })
        else:
            print(request.POST)
            session = request.POST['student']
            action = request.POST.get('action')
            if(action=='buscar'):
                Vstudent = request.POST['student']
                student = Student.objects.all().get(code=Vstudent)
                #actividad = Actividad.objects.all().get(id=request.POST['activity'])
                form = ActivityForm(initial={'student': student})
                return render(request, 'registroActividad.html',{
                    'form': form,
                    "studentInfo": "true",
                    "nombre": student.name,
                    "apellido": student.lastName,
                    'notificaciones': notifi
                    })

            else:    
                #Save the Activity 
                Vstudent = request.POST['student']
                student = Student.objects.all().get(code=Vstudent)
                seguimiento = SeguimientoBeca.objects.all().get(studentID = student)
                
                actividad = Actividad.objects.all().get(id=request.POST['activity'])

                asistencia = AsistenciasActividad.objects.create(seguimientoID = seguimiento, ActividadID = actividad )
                asistencia.save()
                history = HistoryActivityAssistance.objects.create(student=student,activity=actividad)
                history.save()
                form = ActivityForm(initial={'student': session})
                if('Chk' in request.POST):
                    print('Si esta')
                    return render(request, 'registroActividad.html',{
                    'form': form,
                    "studentInfo": "true",
                    "nombre": student.name,
                    "apellido": student.lastName,
                    'notificaciones': notifi
                    })
                else:
                    print('No esta')
                    alert = Alerta.objects.create(title = 'Registro Actividad', type = 4, description = 'Se actualizaron las actividades del estudiante' + request.POST['student'], StudentID = Student.objects.all().get(code = Vstudent))
                    alert.save()
                    return render(request, 'registroActividad.html',{
                    'form': ActivityForm,
                    "alert":True,
                    "studentInfo": "",
                    'notificaciones': notifi
                    })
            
                
        


    
   