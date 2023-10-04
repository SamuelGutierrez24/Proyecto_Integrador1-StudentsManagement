from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student, Materia

def registroNotasBA(request):
    return render(request, 'registroNotasBA.html')

def RegMateria(request):
    if request.method == 'POST':
        codigo_estudiante = request.POST.get('codigo')  # Obtén el nombre del estudiante desde el formulario

        # Buscar al estudiante por su nombre en la base de datos
        estudiante = Student.objects.all().filter(code=codigo_estudiante).exists()
        print(estudiante)
        
        if estudiante == False:
            return  render(request, 'registroNotasBA.html',{
                "error": 'El estudiante no existe'
                })
        else:
            # Recopila los campos generados dinámicamente
            for key, value in request.POST.items():
                if key.startswith('codMateria') and value:
                    index = key.replace('codMateria', '')
                    cod_materia = request.POST[f'codMateria{index}']
                    nota = request.POST[f'Nota{index}']

                    # Crea una instancia de Materia y guárdala en la base de datos
                    materia = Materia(student=Student.objects.all().get(code=codigo_estudiante), codMateria=cod_materia, nota=nota)
                    materia.save()  # Guardar la materia en la base de datos

    return render(request, 'registroNotasBA.html')