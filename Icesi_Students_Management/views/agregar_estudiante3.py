from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Becas

def agregarEstudiante(request):
    # Obtén los datos del formulario almacenados en la sesión
    prev_form_data = request.session.get('form_data', None)
    print("Datos del formulario recuperados en agregar_estudiante:", prev_form_data)
    beca_form_data = request.session.get('button_form_data', None)
    print("Datos del formulario recuperados en agregar_estudiante2:", beca_form_data)
    
    beca = Becas.objects.get(id=beca_form_data)
    
    if request.method == 'POST':
        if 'cancelar' in request.POST:
            # Eliminar todos los datos de la sesión y redirigir a agregar estudiante
            request.session.pop('form_data', None)
            request.session.pop('button_form_data', None)
            return redirect('agregar estudiante')

        elif 'confirmar' in request.POST:
            # Crear el estudiante con la información almacenada en la sesión
            beca = Becas.objects.get(id=beca_form_data)
            nuevo_estudiante = Student.objects.create(
                name = prev_form_data['Nombre'],
                lastName = prev_form_data['Apellido'],
                code = prev_form_data['Codigo'],
                email = prev_form_data['Email'],
                # Ajusta los campos restantes según tu modelo Student
                beca = beca,
            )

            # Eliminar todos los datos de la sesión
            request.session.pop('form_data', None)
            request.session.pop('button_form_data', None)

            # Redirigir a la vista de menú filantropía
            return redirect('menu filantropia')

    return render(request, 'agregar_estudiante3.html', {'prev_form_data': prev_form_data, 'beca_form_data': beca})