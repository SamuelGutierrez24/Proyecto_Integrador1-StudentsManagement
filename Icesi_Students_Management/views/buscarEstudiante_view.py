from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student

def buscarEstudiante(request):
    if request.method == 'POST':
        codigo_estudiante = request.POST.get('inputBuscarEstud')

        # Buscar al estudiante por su nombre en la base de datos
        estudiante = Student.objects.all().filter(code=codigo_estudiante).exists()
        
        if estudiante == False:
            return  render(request, 'buscarEstudiante.html',{
                "error": 'El estudiante no existe'
                })
        else:
            nombre = Student.objects.all().get(code=codigo_estudiante).name
            apellido = Student.objects.all().get(code=codigo_estudiante).lastName
            codigo = Student.objects.all().get(code=codigo_estudiante).code

            request.session['estudData'] = {'nombre': nombre, 'apellido': apellido, 'codigo': codigo}
            return redirect('registroNotasBA.html')
    
    return render(request, 'buscarEstudiante.html')