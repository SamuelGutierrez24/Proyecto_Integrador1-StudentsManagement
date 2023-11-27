from django.shortcuts import render
from Icesi_Students_Management.models import Alerta, Student, Donante
from Icesi_Students_Management.forms import modificarAlerta
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 2


@login_required
@user_passes_test(rol_check, "/signin/")
def alerta(request, noti_id):
    error = ""
    noti = Alerta.objects.get(id=noti_id)

    # 1. Obtener el Student asociado a la Alerta
    student = Student.objects.get(id=noti.StudentID_id)  # Student asociado a la Alerta

    # 2. Obtener el Donante asociado al Student a través de la relación de beca
    donante = Donante.objects.get(typeBecas=student.beca)

    # Excluye la opción "None" del campo Type
    choices = [(value, label) for value, label in Alerta.Type_alert.choices if value != Alerta.Type_alert.NNULL]

    initial_data = {
        'Title': noti.title,
        'Type': noti.type,
        'Description': noti.description,
        'Email': donante.email,  # Usar el correo electrónico del Donante
    }

    if request.method == 'POST':
        form = modificarAlerta(request.POST, initial=initial_data)
        if form.is_valid():
            # Procesa el formulario si es válido
            # Guardar los datos en la sesión
            request.session['form_data'] = form.cleaned_data
        else:
            error = "Hubo errores en el formulario. Revísalo y corrige los campos incorrectos."
    else:
        form = modificarAlerta(initial=initial_data)

    # Elimina la opción "None" del campo Type en el formulario
    form.fields['Type'].choices = choices

    return render(request, 'notificacionEditable.html', {'form': form, 'error': error, 'noti': noti})