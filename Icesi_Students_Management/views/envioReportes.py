from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from Icesi_Students_Management.models import Donante
from ..forms import enviarReporte
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def envioReporte(request):
    if request.method == 'POST':
        form = enviarReporte(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            email = request.POST['email']
            description = request.POST['description']
            seguimientoBeca = request.FILES.get('seguimientoBeca')

            emailMessage = EmailMessage(
                subject=title,
                body=description,
                from_email=settings.EMAIL_HOST_USER,
                to=[email],
            )

            if seguimientoBeca:
                emailMessage.attach(seguimientoBeca.name, seguimientoBeca.read(), seguimientoBeca.content_type)

            emailMessage.send(fail_silently=False)
            
            messages.success(request,'Correo enviado con éxito')

            return redirect('envioReportes.html')
    else:
        return render(request, 'envioReportes.html',{
        'form': enviarReporte
    })

