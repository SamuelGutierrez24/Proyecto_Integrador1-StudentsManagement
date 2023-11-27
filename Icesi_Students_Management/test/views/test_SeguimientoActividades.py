from django.test import TestCase
from Icesi_Students_Management.forms import *
from django.urls import reverse
# Create your tests here.
class registroActividadTestCase(TestCase):

    
        

    def test_creacion_actividad(self):
        beca = Becas.objects.create(type = 'Completa', percentage = '100', description='Beca completa', alimentacion= True, transporte = True)
        estudiante = Student.objects.create(id= 2, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id= '1')
        semester = Semester.objects.create(name='2023-1')
        carrera = Carrera.objects.create(nameCarrera = 'Ingenieria de sistemas', carreraID = '1', precioMatricula= 10000000)
        seguimientoBeca = SeguimientoBeca.objects.create(testimonio = 'Agradecido', studentID = estudiante, SemesterID = semester, carreraID=carrera)
        activity = Actividad.objects.create(nombre='Porrismo')
        asistencia = AsistenciasActividad.objects.create(seguimientoID=seguimientoBeca,ActividadID=activity)
        self.assertEquals(asistencia.ActividadID,activity)
        self.assertEqual(asistencia.seguimientoID,seguimientoBeca)

    def test_vista_registrarActividad(self):
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=3)
        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, reverse('bienestarUniversitario'))

        response = self.client.get(reverse('registroActividades'))
        print(response)
        self.assertEquals(response.status_code,200)

    def test_valid_Activity_form(self):
        beca = Becas.objects.create(type = 'Completa', percentage = '100', description='Beca completa', alimentacion= True, transporte = True)
        estudiante = Student.objects.create(id= 2, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id= '1')
        semester = Semester.objects.create(name='2023-1')
        carrera = Carrera.objects.create(nameCarrera = 'Ingenieria de sistemas', carreraID = '1', precioMatricula= 10000000)
        seguimientoBeca = SeguimientoBeca.objects.create(testimonio = 'Agradecido', studentID = estudiante, SemesterID = semester, carreraID=carrera)
        activity = Actividad.objects.create(id = '1', nombre='Porrismo', tipo= 1)
        data= {
            'student': 'A00381035', 
            'activity': '1',

        }
        form = ActivityForm(data=data)
        self.assertTrue(form.is_valid())

