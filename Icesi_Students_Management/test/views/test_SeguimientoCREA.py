from django.test import TestCase
from Icesi_Students_Management.forms import *
from django.urls import reverse
# Create your tests here.
class registroActividadTestCase(TestCase):

    
        

    def test_creation_CREAactivity(self):
        beca = Becas.objects.create(type = 'Completa', percentage = '100', description='Beca completa', alimentacion= True, transporte = True)
        estudiante = Student.objects.create(id= 2, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id= '1')
        semester = Semester.objects.create(name='2023-1')
        carrera = Carrera.objects.create(nameCarrera = 'Ingenieria de sistemas', carreraID = '1', precioMatricula= 10000000)
        seguimientoBeca = SeguimientoBeca.objects.create(testimonio = 'Agradecido', studentID = estudiante, SemesterID = semester, carreraID=carrera)
        activity = Actividad.objects.create(nombre='Centro LEO')
        asistencia = AsistenciaCREA.objects.create(activity=activity,seguimiento=seguimientoBeca,reason='I dont know how read')
        self.assertEquals(asistencia.activity,activity)
        self.assertEqual(asistencia.seguimiento,seguimientoBeca)

    def test_vista_registrarActividad(self):
        self.user2 = User.objects.create_user(username='user2', password='password2', rol=6)
        data = {
            'username': 'user2',
            'password': 'password2'
        }
        response = self.client.post(reverse('signin'), data)
        self.assertRedirects(response, reverse('crea'))

        response = self.client.get(reverse('registerCrea'))
        print(response)
        self.assertEquals(response.status_code,200)

    def test_valid_CREA_form(self):
        beca = Becas.objects.create(type = 'Completa', percentage = '100', description='Beca completa', alimentacion= True, transporte = True)
        estudiante = Student.objects.create(id= 2, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id= '1')
        semester = Semester.objects.create(name='2023-1')
        carrera = Carrera.objects.create(nameCarrera = 'Ingenieria de sistemas', carreraID = '1', precioMatricula= 10000000)
        seguimientoBeca = SeguimientoBeca.objects.create(testimonio = 'Agradecido', studentID = estudiante, SemesterID = semester, carreraID=carrera)
        activity = Actividad.objects.create(nombre='Centro LEO', tipo = 2)
        data= {
            'student': 'A00381035', 
            'activity': '1',
            'reason': 'I dont know how read',

        }
        form = CreaForm(data=data)
        self.assertTrue(form.is_valid())

