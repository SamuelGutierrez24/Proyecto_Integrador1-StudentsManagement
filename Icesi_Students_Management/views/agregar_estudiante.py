from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.forms import addStudent

def agregarInformacionEscrita(request):
    if request.method == 'POST':
        form = addStudent(request.POST)
        print(request.POST)
        if form.is_valid():
            # Almacenar los datos del formulario en la sesión
            request.session['form_data'] = form.cleaned_data
            print("Datos del formulario almacenados en la sesión:", request.session.get('form_data', None))

            # Verificar si el código ya existe en la base de datos
            codigo = form.cleaned_data['Codigo']
            studentCode = Student.objects.filter(code=codigo).exists()
            if studentCode:
                return render(request, 'agregar_estudiante.html', {'form': addStudent, 'error': "El código ya está en uso"})
            else:
                # Redirigir a la vista agregar_estudiante2.html
                return redirect('agregar estudiante 2')

    return render(request, 'agregar_estudiante.html', {'form': addStudent})