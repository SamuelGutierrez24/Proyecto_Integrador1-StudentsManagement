from django.test import TestCase, Client
from django.urls import reverse
from Icesi_Students_Management.models import Actividad
from Icesi_Students_Management.models import AsistenciasActividad
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Becas
from Icesi_Students_Management.forms import ActivityForm
from Icesi_Students_Management.models import SeguimientoBeca
from Icesi_Students_Management.models import Semester
# Create your tests here.
class registroActividadTestCase(TestCase):

    
        

    def test_creacion_actividad(self):
        beca = Becas.objects.create(type = 'Completa', percentage = '100', description='Beca completa', alimentacion= True, transporte = True)
        estudiante = Student.objects.create(id= 2, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id= '1')
        semester = Semester.objects.create(name='2023-1')
        seguimientoBeca = SeguimientoBeca.objects.create(testimonio = 'Agradecido', studentID = estudiante, SemesterID = semester)
        activity = Actividad.objects.create(nombre='Porrismo')
        asistencia = AsistenciasActividad.objects.create(seguimientoID=seguimientoBeca,ActividadID=activity)
        self.assertEquals(asistencia.ActividadID,activity)
        self.assertEqual(asistencia.seguimientoID,seguimientoBeca)

    def test_vista_registrarActividad(self):
        response = self.client.get(reverse('registroActividades'))
        print(response)
        self.assertEquals(response.status_code,200)

    def test_valid_Activity_form(self):
        beca = Becas.objects.create(type = 'Completa', percentage = '100', description='Beca completa', alimentacion= True, transporte = True)
        estudiante = Student.objects.create(id= 2, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id= '1')
        semester = Semester.objects.create(name='2023-1')
        seguimientoBeca = SeguimientoBeca.objects.create(testimonio = 'Agradecido', studentID = estudiante, SemesterID = semester)
        activity = Actividad.objects.create(nombre='Porrismo')
        data= {
            'student': 'A00381035', 
            'activity': '1',

        }

        form = ActivityForm(data=data)
        
        self.assertTrue(form.is_valid())

