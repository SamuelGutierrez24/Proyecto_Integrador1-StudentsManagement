from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMessage
from ..forms import modificarAlerta
from django.contrib import messages
from django.conf import settings
from django.core.files.base import ContentFile
from ..models import *
from .utils import createPDF

def sendAlert(request, noti_id):
    if request.method == 'POST':
        form = modificarAlerta(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['Title']
            email = request.POST['Email']
            description = request.POST['Description']
            Type = request.POST['Type']

            alerta = Alerta.objects.get(id=noti_id)
            student = alerta.StudentID
            typeContent = ""
            if Type == 0:
                typeContent = "None"
            elif Type == 1:
                typeContent = "Actualizacion de informacion contabilida"
            elif Type == 2:
                typeContent = "Actualizacion de informacion Bienestar Universitario"
            elif Type == 3:
                typeContent = "Actualizacion de informacion Director de programa"
            else:
                typeContent = "Actualización de actividades no academicas de un estudiante"
            data = {
                'Title': title,
                'Type': typeContent,
                'Description': description,
                'Email': email,  # Usar el correo electrónico del Donante
                'student':student
            }
            
            pdf = createPDF('sendNotificationStyle.html', data)
            emailMessage = EmailMessage(
            subject='Notificacion acerca de Estudiante',
            body='En el presente correo se encuentra adjunto información acerca del estudiante al cual provee la beca',
            from_email=settings.EMAIL_HOST_USER,
            to=[email],
                            )
            pdfContent = pdf.content
            seguimientoBeca = ContentFile(pdfContent, name='Alerta_Estudiante.pdf')

            emailMessage.attach('Alerta_Estudiante.pdf', seguimientoBeca.read(), 'application/pdf')
            emailMessage.send(fail_silently=False)
            messages.success(request, 'Alerta enviada con éxito')
            notificacion = get_object_or_404(Alerta, id=noti_id)
            notificacion.delete()
        return redirect('/menu_filantropia')
            
    else:
        return render(request, 'menu_filantropia.html', {
            'form': modificarAlerta
        })                 
                    
                    
