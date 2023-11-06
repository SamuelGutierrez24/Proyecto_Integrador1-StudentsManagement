from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from ..forms import enviarReporte
from django.contrib import messages
from django.conf import settings
from django.core.files.base import ContentFile
from .utils import createPDF
from ..models import *
   
def sendReport(request):
    if request.method == 'POST':
        form = enviarReporte(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            email = request.POST['email']
            description = request.POST['description']
            allDonor = request.POST.get('allDonor', False)
            seguimientoBeca = request.FILES.get('seguimientoBeca')
            #PARA TODOS LOS DONANTES
            if allDonor:
                donors = Donante.objects.all()
                emailArray = []
                for donor in donors:
                    emailArray.append(donor.email)
                    students = Student.objects.filter(beca=donor.typeBecas)
                    for student in students:
                        scholarship = SeguimientoBeca.objects.get(studentID = student.id)
                        finanInfo = InformacionFinanciera.objects.get(seguimientoBecaID = scholarship.id)
                        academicBalance = BalanceAcademico.objects.get(SeguimientoBecaID = scholarship.id)
                        data = {
                            'student': student,
                            'finanInfo': finanInfo,
                            'academicBalance':academicBalance
                        }
                        pdf = createPDF('estiloSB.html', data)
                        emailMessage = EmailMessage(
                                subject=title,
                                body=description,
                                from_email=settings.EMAIL_HOST_USER,
                                to=[donor.email],
                            )
                        pdfContent = pdf.content
                        seguimientoBeca = ContentFile(pdfContent, name='Seguimiento_beca.pdf')

                        emailMessage.attach('Seguimiento_beca.pdf', seguimientoBeca.read(), 'application/pdf')
                        emailMessage.send(fail_silently=False)
                messages.success(request, 'Correo enviado con éxito')
            else:
                #PARA UN SOLO DONANTE
                donor = Donante.objects.filter(email=email)
                if donor.exists():
                    donor = Donante.objects.get(email=email)
                    students = Student.objects.filter(beca=donor.typeBecas)
                    for student in students:
                        scholarship = SeguimientoBeca.objects.get(studentID = student.id)
                        finanInfo = InformacionFinanciera.objects.get(seguimientoBecaID = scholarship.id)
                        academicBalance = BalanceAcademico.objects.get(SeguimientoBecaID = scholarship.id)
                        data = {
                            'student': student,
                            'finanInfo': finanInfo,
                            'academicBalance':academicBalance
                        }
                        pdf = createPDF('estiloSB.html', data)
                        emailMessage = EmailMessage(
                                subject=title,
                                body=description,
                                from_email=settings.EMAIL_HOST_USER,
                                to=[donor.email],
                            )
                        pdfContent = pdf.content
                        seguimientoBeca = ContentFile(pdfContent, name='Seguimiento_beca.pdf')

                        emailMessage.attach('Seguimiento_beca.pdf', seguimientoBeca.read(), 'application/pdf')
                        emailMessage.send(fail_silently=False)
                        
                    messages.success(request, 'Correo enviado con éxito')
                else:
                    messages.error(request, 'El correo del donador no se encuentra registrado!')

            return redirect('envioReportes.html')
    else:
        return render(request, 'envioReportes.html', {
            'form': enviarReporte
        })                 
                    
                    
