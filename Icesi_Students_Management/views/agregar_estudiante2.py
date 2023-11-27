from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Becas
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 2


@login_required
@user_passes_test(rol_check, "/signin/")
def agregarInformacionBoton(request):
    becas = Becas.objects.all()
    # Imprimir la sesión completa
    print("Contenido de la sesión en agregar_estudiante2:", request.session.items())

    # Obtén los datos del formulario almacenados en la sesión
    prev_form_data = request.session.get('form_data', None)
    print("Datos del formulario recuperados en agregar_estudiante2:", prev_form_data)

    print(request.POST)
    
    if request.method == 'POST':
        # Verificar si se ha seleccionado una beca
        selected_beca_id = request.POST.get('selected_button', None)
        print(selected_beca_id)

        if selected_beca_id is not None and selected_beca_id is not '':
            request.session['button_form_data'] = selected_beca_id

            # Redirigir a la vista agregar_estudiante3.html
            return redirect('agregar estudiante 3')
        else:
            messages.error(request, 'Cuidado! Beca no seleccionada')
            
            return render(request, 'agregar_estudiante2.html', {'Becas': becas})
    
    return render(request, 'agregar_estudiante2.html', {'Becas': becas})