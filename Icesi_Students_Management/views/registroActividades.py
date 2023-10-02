from django.shortcuts import render, redirect
from django.http import HttpResponse
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Actividad
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
            #Save the Activity 
            porProbar = ActivityForm(request.POST)
            porProbar.save()
            if('Chk' in request.POST):
                print('Si esta')
                return render(request, 'registroActividad.html',{
                'form': ActivityForm
                })
            else:
                print('No esta')
                return redirect('bienestarUniversitario')
                
        


    
   