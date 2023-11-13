from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Becas
from Icesi_Students_Management.forms import addStudent
from Icesi_Students_Management.models import InformacionFinanciera
from Icesi_Students_Management.models import SeguimientoBeca
from Icesi_Students_Management.models import Carrera, Semester
import datetime

def agregar(request):
    becas = Becas.objects.all()
    careers = Carrera.objects.all()
    if request.method == 'POST':
        form = addStudent(request.POST)
        if form.is_valid():
            # Almacenar los datos del formulario en la sesión
            request.session['form_data'] = form.cleaned_data
            print(request.POST.get("selected_button"))
            request.session['selected_button'] = request.POST.get('selected_button')

            # Verificar si el código ya existe en la base de datos
            codigo = request.POST['Codigo']
            semester = request.POST['semester']
            careerID = form.cleaned_data['career']
            careerSelected = Carrera.objects.get(carreraID=careerID)
            studentCode = Student.objects.all().filter(code=codigo).exists()
            if studentCode:
                # El código ya está en uso, puedes manejar este caso según tus necesidades
                # Por ejemplo, mostrar un mensaje de error o redirigir a otra página
                # Aquí solo se imprime un mensaje de error en la consola
                return render(request, 'agregar_estudiante.html', {'form': addStudent, 'Becas': becas, 'error': "El código ya está en uso"})
            else:
                # El código no está en uso, crear el objeto Student
                student_data = request.session['form_data']
                selected_button = request.session['selected_button']
                beca = Becas.objects.all().get(id=selected_button)
                Student.objects.create(name=student_data['Nombre'], lastName=student_data['Apellido'], email=student_data['Email'], code=codigo, beca=beca)
                print("ESTE ES EL ID DEL ESTUDIANTEEEEEEEEEEEEEEEE: ",Student.objects.get(code=codigo).id)
                
                #Creacion del seguimiento de beca del estudiante
                SeguimientoBeca.objects.create(studentID=Student.objects.get(code=codigo),SemesterID=Semester.objects.get(name=semester),carreraID=careerSelected)



                #Creacion de la informacion financiera del estudiante
                estudiante = Student.objects.get(code=codigo)
                seguimiento_beca = SeguimientoBeca.objects.get(
                    studentID=estudiante)
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

                InformacionFinanciera.objects.create(studentID=codigo,
                                                    type=beca,
                                                    dineroAsignado=dineroTotal,
                                                    matriculaBeca=dineroMatricula,
                                                    transporteBeca=dineroTransporte,
                                                    alimentacionBeca=dineroAlimentacion,
                                                    gasto=gastoTotal,
                                                    fecha=datetime.datetime.now().strftime('%Y-%m-%d'),
                                                    seguimientoBecaID=seguimiento_beca)


                # Limpiar la sesión
                request.session.clear()
                
                return redirect('menu filantropia')
            
    return render(request, 'agregar_estudiante.html', {'form': addStudent, 'Becas': becas})
