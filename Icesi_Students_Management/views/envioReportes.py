from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from ..forms import enviarReporte
from django.contrib import messages
from django.conf import settings
from django.core.files.base import ContentFile
from .utils import createPDF
from ..models import *
from django.contrib.auth.decorators import user_passes_test, login_required


def rol_check(user):
    return user.rol == 2


@login_required
@user_passes_test(rol_check, "/signin/")
def sendReport(request):
    notificaciones = Alerta.objects.all()
    notifi = []

    for noti in notificaciones:
        if(noti.type==4):
            notifi.append(noti)
    if request.method == 'POST':
        form = enviarReporte(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST['title']
            email = request.POST['email']
            description = request.POST['description']
            allFields = request.POST.get('todosLosCampos', False)
            academicInfo = request.POST.get('informacionAcademica', False)
            finantialInfo = request.POST.get('informacionFinanciera', False)
            noAcademicInfo = request.POST.get('informacionNoAcademica', False)
            testomonyStudent = request.POST.get('testimonioEstudiante', False)

            arrayFields = [allFields, academicInfo, finantialInfo, noAcademicInfo, testomonyStudent]

            if arrayFields.__contains__('on'):
                        
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
                        infoFinanHisto = HistorialGastos.objects.filter(informacion_financiera = finanInfo.informeID)

                        if academicInfo != False:
                            try:
                                academicBalance = BalanceAcademico.objects.filter(SeguimientoBecaID=scholarship.id)
                            except BalanceAcademico.DoesNotExist:
                                messages.error(request, 'El estudiante no tiene la información académica registrada')
                                return redirect('envioReportes.html')
                        else:
                            academicBalance = BalanceAcademico.objects.filter(SeguimientoBecaID=scholarship.id)
                        
                        if noAcademicInfo != False:
                            try:
                                noAcademicActivity = AsistenciasActividad.objects.filter(seguimientoID=scholarship.id)
                            except AsistenciasActividad.DoesNotExist:
                                messages.error(request, 'El estudiante no tiene la información no académica registrada')
                                return redirect('envioReportes.html')
                        else:
                            noAcademicActivity = AsistenciasActividad.objects.filter(seguimientoID=scholarship.id)


                        data = {
                        'student': student,
                        'finanInfo': finanInfo,
                        'infoFinanHisto':infoFinanHisto,
                        'academicBalance':academicBalance,
                        'academicInfo': academicInfo,
                        'finantialInfo': finantialInfo,
                        'noAcademicInfo': noAcademicInfo,
                        'noAcademicActivity':noAcademicActivity,
                        'testomonyStudent': testomonyStudent,
                        'scholarship':scholarship
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
                  return redirect('envioReportes.html')
              else:
                  #PARA UN SOLO DONANTE
                  donor = Donante.objects.filter(email=email)
                  if donor.exists():
                      donor = Donante.objects.get(email=email)
                      students = Student.objects.filter(beca=donor.typeBecas)
                      for student in students:
                        scholarship = SeguimientoBeca.objects.get(studentID = student.id)
                        finanInfo = InformacionFinanciera.objects.get(seguimientoBecaID = scholarship.id)
                        infoFinanHisto = HistorialGastos.objects.filter(informacion_financiera = finanInfo.informeID)
                        
                        if academicInfo != False:
                            try:
                                academicBalance = BalanceAcademico.objects.filter(SeguimientoBecaID=scholarship.id)
                            except BalanceAcademico.DoesNotExist:
                                messages.error(request, 'El estudiante no tiene la información académica registrada')
                                return redirect('envioReportes.html')
                        else:
                            academicBalance = BalanceAcademico.objects.filter(SeguimientoBecaID=scholarship.id)
                        
                        if noAcademicInfo != False:
                            try:
                                noAcademicActivity = AsistenciasActividad.objects.filter(seguimientoID=scholarship.id)
                            except AsistenciasActividad.DoesNotExist:
                                messages.error(request, 'El estudiante no tiene la información no académica registrada')
                                return redirect('envioReportes.html')
                        else:
                            noAcademicActivity = AsistenciasActividad.objects.filter(seguimientoID=scholarship.id)


                        data = {
                        'student': student,
                        'finanInfo': finanInfo,
                        'infoFinanHisto':infoFinanHisto,
                        'academicBalance':academicBalance,
                        'academicInfo': academicInfo,
                        'finantialInfo': finantialInfo,
                        'noAcademicInfo': noAcademicInfo,
                        'noAcademicActivity':noAcademicActivity,
                        'testomonyStudent': testomonyStudent,
                        'scholarship':scholarship
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
                      return redirect('envioReportes.html')
                  else:
                      messages.error(request, 'El correo del donador no se encuentra registrado!')
                      return redirect('envioReportes.html')
            else:
                messages.error(request, 'Debe seleccionar alguno de los campos para enviar el informe!')
                return redirect('envioReportes.html')
    else:
        return render(request, 'envioReportes.html', {
            'form': enviarReporte,'notificaciones': notifi
        })                 
                    
                    
