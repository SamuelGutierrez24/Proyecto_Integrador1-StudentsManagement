from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from ..forms import enviarReporte
from django.contrib import messages
from django.conf import settings
from django.core.files.base import ContentFile
from .utils import createPDF
from ..models import *

def envioReporte(request):
    if request.method == 'POST':
        form = enviarReporte(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            email = request.POST['email']
            description = request.POST['description']
            todosDonantes = request.POST.get('todosDonantes', False)
            seguimientoBeca = request.FILES.get('seguimientoBeca')

            if todosDonantes:
                donantes = Donante.objects.all()
                emailArray = []
                pdfs = []

                for donante in donantes:
                    emailArray.append(donante.email)
                    estudiante = Student.objects.filter(beca=donante.typeBecas)
                    data = {
                        'estudiante': estudiante
                    }
                    pdf = createPDF('estiloSB.html', data)
                    pdfs.append(pdf)
                
                for i, email in enumerate(emailArray):
                    emailMessage = EmailMessage(
                        subject=title,
                        body=description,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[email],
                    )
                    pdf = pdfs[i]
                    pdfContent = pdf.content
                    seguimientoBeca = ContentFile(pdfContent, name='Seguimiento_beca.pdf')

                    emailMessage.attach('Seguimiento_beca.pdf', seguimientoBeca.read(), 'application/pdf')
                    emailMessage.send(fail_silently=False)
                messages.success(request, 'Correo enviado con éxito')
            
            else:
                donante = Donante.objects.filter(email=email)
                if donante.exists():
                    donante = Donante.objects.get(email=email)
                    estudiante = Student.objects.filter(beca=donante.typeBecas)
                    
                    data = {
                        'estudiante': estudiante
                    }
                    pdf = createPDF('estiloSB.html', data)
                    pdfContent = pdf.content
                    
                    seguimientoBeca = ContentFile(pdfContent, name='Seguimiento_beca')

                    #En esta parte se crea el correo
                    emailMessage = EmailMessage(
                        subject=title,
                        body=description,
                        from_email=settings.EMAIL_HOST_USER,
                        to=[email],
                    )
                    #Aqui se le añade el pdf al correo
                    emailMessage.attach('Seguimiento_beca', seguimientoBeca.read(), 'application/pdf')

                    #En esta parte se envia el correo
                    emailMessage.send(fail_silently=False)
                    messages.success(request, 'Correo enviado con éxito')
                else:
                    messages.error(request, 'El correo del donador no se encuentra registrado!')

            return redirect('envioReportes.html')
    else:
        return render(request, 'envioReportes.html', {
            'form': enviarReporte
        })
