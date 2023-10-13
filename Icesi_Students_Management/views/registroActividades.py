from django.shortcuts import render, redirect
from django.http import HttpResponse
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Actividad
from Icesi_Students_Management.models import AsistenciasActividad
from Icesi_Students_Management.models import SeguimientoBeca
from Icesi_Students_Management.models import Alerta
from Icesi_Students_Management.models import User
from Icesi_Students_Management.forms import ActivityForm

def registroA(request):
    
    if request.method == 'GET':
        print('enviando formulario')
        return render(request, 'registroActividad.html',{
                'form': ActivityForm
                })
    else:
        studentToVerify = request.POST['student']
        studentInDB = Student.objects.all().filter(code=studentToVerify).exists()
        print(studentInDB)
        if studentInDB == False:
             return  render(request, 'registroActividad.html',{
                'form': ActivityForm,
                "error": 'El estudiante no existe'
                })
        else:
            print(request.POST)
            #Save the Activity 
            Vstudent = request.POST['student']
            student = Student.objects.all().get(code=Vstudent)
            seguimiento = SeguimientoBeca.objects.all().get(studentID = student)
            
            actividad = Actividad.objects.all().get(id=request.POST['activity'])

            asistencia = AsistenciasActividad.objects.create(seguimientoID = seguimiento, ActividadID = actividad )
            asistencia.save()
            if('Chk' in request.POST):
                print('Si esta')
                return render(request, 'registroActividad.html',{
                'form': ActivityForm
                })
            else:
                print('No esta')
                alert = Alerta.objects.create(title = 'Registro Actividad', type = 4, description = 'Se actualizaron las actividades del estudiante' + request.POST['student'])
                alert.save()
                return render(request, 'registroActividad.html',{
                'form': ActivityForm,
                "alert":True
                })
            
                
        


    
   