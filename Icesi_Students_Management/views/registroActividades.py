from django.shortcuts import render, redirect
from django.http import HttpResponse
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Actividad
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
            actividad = Actividad.objects.create(student = Student.objects.all().get(code=Vstudent),name = request.POST['name'],assists = request.POST['assists'])
            actividad.save()
            if('Chk' in request.POST):
                print('Si esta')
                return render(request, 'registroActividad.html',{
                'form': ActivityForm
                })
            else:
                print('No esta')
                alert = Alerta.objects.create(title = 'Registro Acticidad', type = 3, description = 'Se actualizaron las actividades del estudiante' + request.POST['student'], userID = User.objects.all().get(id = 1))
                alert.save()
                return render(request, 'registroActividad.html',{
                'form': ActivityForm,
                "alert":True
                })
            
                
        


    
   