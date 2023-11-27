from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Becas
from Icesi_Students_Management.models import SeguimientoBeca
from Icesi_Students_Management.models import Semester
from Icesi_Students_Management.models import Carrera
from Icesi_Students_Management.models import InformacionFinanciera
from django.contrib import messages
import datetime
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 2


@login_required
@user_passes_test(rol_check, "/signin/")
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
            beca = Becas.objects.get(id = beca_form_data)
            Student.objects.create(
                name = prev_form_data['Nombre'],
                lastName = prev_form_data['Apellido'],
                code = prev_form_data['Codigo'],
                email = prev_form_data['Email'],
                # Ajusta los campos restantes según tu modelo Student
                beca = beca,
            )
            
            # Crear el seguimiento con la información almacenada en la sesión
            SeguimientoBeca.objects.create(
                studentID = Student.objects.get(code = prev_form_data['Codigo']),
                SemesterID = Semester.objects.get(name = prev_form_data['semester']),
                carreraID = Carrera.objects.get(carreraID = prev_form_data['career'])
            )
            
            #Creacion de la informacion financiera del estudiante
            estudiante = Student.objects.get(code = prev_form_data['Codigo'])
            seguimiento_beca = SeguimientoBeca.objects.get(studentID = estudiante)
            beca = estudiante.beca.type

            gastoTotal = 0
            dineroTransporte = 0
            dineroAlimentacion = 0
            dineroMatricula = (estudiante.beca.percentage/100) * float(seguimiento_beca.carreraID.precioMatricula)
                
            dineroTotal = dineroMatricula

            if estudiante.beca.alimentacion == True:
                dineroTotal = dineroTotal + 800000
                dineroAlimentacion = dineroAlimentacion + 800000
            if estudiante.beca.transporte == True:
                dineroTotal = dineroTotal + 432000
                dineroTransporte = dineroTransporte + 432000
            InformacionFinanciera.objects.create(
                studentID = prev_form_data['Codigo'],
                type = beca,
                dineroAsignado = dineroTotal,
                matriculaBeca = dineroMatricula,
                transporteBeca = dineroTransporte,
                alimentacionBeca = dineroAlimentacion,
                gasto = gastoTotal,
                fecha = datetime.datetime.now().strftime('%Y-%m-%d'),
                seguimientoBecaID = seguimiento_beca
            )
            
            # Eliminar todos los datos de la sesión
            request.session.pop('form_data', None)
            request.session.pop('button_form_data', None)
            
            messages.success(request, 'Estudiante creado con exito!')

            # Redirigir a la vista de menú filantropía
            return redirect('menu filantropia')

    return render(request, 'agregar_estudiante3.html', {'prev_form_data': prev_form_data, 'beca_form_data': beca})