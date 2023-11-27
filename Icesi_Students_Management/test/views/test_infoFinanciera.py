from django.test import TestCase, Client
from django.urls import reverse
from Icesi_Students_Management.models import *
from datetime import datetime
from Icesi_Students_Management.forms import registrarInfoFinanciera

class InfofinancieraTestCase(TestCase):

    def test_Creacion_Info_Financiera(self):
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=4)
        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, reverse('menuContabilidad'))

        # Carreras
        carrera = Carrera.objects.create(nameCarrera="Ingenieria de Sistemas", carreraID="SIS-007", precioMatricula=12730000)

        # Becas
        beca = Becas.objects.create(type="Ser pilo paga", percentage=100, description="Esta beca te da toda la matricula, el transporte y la alimentacion", alimentacion=True, transporte=True)

        # Informacion del estudiante
        student = Student.objects.create(id=12, name="Luis Fernando", lastName="Pinillos Sanchez", code="A00381323", email="luis@gmail.com", beca=beca)

        # Semestre
        semestre = Semester.objects.create(name = "5")

        # Seguimiento de beca
        seguimientoBeca = SeguimientoBeca.objects.create(testimonio="Me gusta mucho mi beca", studentID = student, SemesterID = semestre, carreraID = carrera)
        
        # Para llenar el valor monetario de cada cosa
        dineroTransporte = 0
        dineroAlimentacion = 0
        dineroMatricula = (student.beca.percentage/100) * float(seguimientoBeca.carreraID.precioMatricula)
                
        dineroTotal = dineroMatricula

        if student.beca.alimentacion:
            dineroTotal += 800000
            dineroAlimentacion += 800000

        if student.beca.transporte:
            dineroTotal += 432000
            dineroTransporte += 432000

        # Informacion financiera
        fecha = datetime(2023, 10, 14).date()
        informacionFinanciera = InformacionFinanciera.objects.create(studentID = student,
                                                                     type = beca.type,
                                                                     dineroAsignado = dineroTotal,
                                                                     matriculaBeca = dineroMatricula,
                                                                     transporteBeca = dineroTransporte,
                                                                     alimentacionBeca = dineroAlimentacion,
                                                                     gasto = 0,
                                                                     fecha = fecha,
                                                                     seguimientoBecaID = seguimientoBeca
                                                                     )
        
        data= {
            'studentID': 'A00381323', 
            'type': 'Ser pilo paga',
            'matriculaBeca':12730000,
            'transporteBeca':432000,
            'alimentacionBeca':800000,
            'dineroAsignado':13962000,
            'gasto':0,
            'fecha':fecha,
            'categoriaGasto':'matricula'

        }
        form = registrarInfoFinanciera(data=data)
        self.assertTrue(form.is_valid())

    
    def test_vista_menuConta(self):
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=4)
        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, reverse('menuContabilidad'))

        response = self.client.get(reverse('menuContabilidad'))
        print(response)
        self.assertEquals(response.status_code,200)

    def test_vista_infoFinanciera(self):
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=4)
        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, reverse('menuContabilidad'))

        response = self.client.get(reverse('infoFinanciera'))
        print(response)
        self.assertEquals(response.status_code,200)

    def test_vista_buscarEstud(self):
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=4)
        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, reverse('menuContabilidad'))

        response = self.client.get(reverse('buscarEstud'))
        print(response)
        self.assertEquals(response.status_code,200)

    def test_vista_modificar(self):
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=4)
        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, reverse('menuContabilidad'))

        response = self.client.get(reverse('modificarInfo', kwargs={'code': 'A00381323'}))
        print(response)
        self.assertEquals(response.status_code,302)#Se coloca 302 debido a que este significa found, lo cual nos dice que se encontro la url con el codigo dado

    def test_Actualizacion_Info_Financiera(self):
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=4)
        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, reverse('menuContabilidad'))

        # Carreras
        carrera = Carrera.objects.create(nameCarrera="Ingenieria de Sistemas", carreraID="SIS-007", precioMatricula=12730000)

        # Becas
        beca = Becas.objects.create(type="Ser pilo paga", percentage=100, description="Esta beca te da toda la matricula, el transporte y la alimentacion", alimentacion=True, transporte=True)

        # Informacion del estudiante
        student = Student.objects.create(id=12, name="Luis Fernando", lastName="Pinillos Sanchez", code="A00381323", email="luis@gmail.com", beca=beca)

        # Semestre
        semestre = Semester.objects.create(name = "5")

        # Seguimiento de beca
        seguimientoBeca = SeguimientoBeca.objects.create(testimonio="Me gusta mucho mi beca", studentID = student, SemesterID = semestre, carreraID = carrera)
        
        # Para llenar el valor monetario de cada cosa
        dineroTransporte = 0
        dineroAlimentacion = 0
        dineroMatricula = (student.beca.percentage/100) * float(seguimientoBeca.carreraID.precioMatricula)
                
        dineroTotal = dineroMatricula

        if student.beca.alimentacion:
            dineroTotal += 800000
            dineroAlimentacion += 800000

        if student.beca.transporte:
            dineroTotal += 432000
            dineroTransporte += 432000

        # Informacion financiera
        fecha = datetime(2023, 10, 14).date()
        informacionFinanciera = InformacionFinanciera.objects.create(studentID = student,
                                                                     type = beca.type,
                                                                     dineroAsignado = dineroTotal,
                                                                     matriculaBeca = dineroMatricula,
                                                                     transporteBeca = dineroTransporte,
                                                                     alimentacionBeca = dineroAlimentacion,
                                                                     gasto = 0,
                                                                     fecha = fecha,
                                                                     seguimientoBecaID = seguimientoBeca
                                                                     )
       
        fecha = datetime(2023,11,18)

        # Datos para la actualización
        updatedData = {
            'studentID': 'A00381323',
            'type': 'Ser pilo paga',
            'matriculaBeca': 10000000, 
            'transporteBeca': 400000,    
            'alimentacionBeca': 750000,  
            'dineroAsignado': 11150000,  
            'gasto': 50000,               
            'fecha': fecha,
            'categoriaGasto': 'transporte'
        }
        form = registrarInfoFinanciera(data=updatedData, instance=informacionFinanciera)
      
        self.assertTrue(form.is_valid())

        updatedInformacionFinanciera = form.save()

        self.assertEqual(updatedInformacionFinanciera.matriculaBeca, 10000000)
        self.assertEqual(updatedInformacionFinanciera.transporteBeca, 400000)
        self.assertEqual(updatedInformacionFinanciera.alimentacionBeca, 750000)
        self.assertEqual(updatedInformacionFinanciera.dineroAsignado, 11150000)
        self.assertEqual(updatedInformacionFinanciera.gasto, 50000)

