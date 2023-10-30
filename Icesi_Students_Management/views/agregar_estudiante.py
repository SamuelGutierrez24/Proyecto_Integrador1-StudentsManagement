from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Becas
from Icesi_Students_Management.forms import addStudent

def agregar(request):
    becas = Becas.objects.all()
    if request.method == 'POST':
        form = addStudent(request.POST)
        if form.is_valid():
            # Almacenar los datos del formulario en la sesión
            request.session['form_data'] = form.cleaned_data
            print(request.POST.get("selected_button"))
            request.session['selected_button'] = request.POST.get('selected_button')

            # Verificar si el código ya existe en la base de datos
            codigo = request.POST['Codigo']
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
                # Limpiar la sesión
                request.session.clear()
                
                return redirect('menu filantropia')
            
    return render(request, 'agregar_estudiante.html', {'form': addStudent, 'Becas': becas})
