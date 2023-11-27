from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.forms import addStudent
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 2


@login_required
@user_passes_test(rol_check, "/signin/")
def agregarInformacionEscrita(request):
    if request.method == 'POST':
        form = addStudent(request.POST)
        print(request.POST)
        if form.is_valid():
            # Almacenar los datos del formulario en la sesión
            request.session['form_data'] = form.cleaned_data
            # Verificar si el código ya existe en la base de datos
            codigo = form.cleaned_data['Codigo']
            studentCode = Student.objects.filter(code=codigo).exists()
            if studentCode:
                messages.error(request, 'Cuidado! El codigo del estudiante ya esta en uso')

                return render(request, 'agregar_estudiante.html', {'form': addStudent})
            else:
                # Redirigir a la vista agregar_estudiante2.html
                return redirect('agregar estudiante 2')

    return render(request, 'agregar_estudiante.html', {'form': addStudent})