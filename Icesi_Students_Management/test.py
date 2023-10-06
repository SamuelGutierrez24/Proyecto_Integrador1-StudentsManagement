from django.test import TestCase, Client
from django.urls import reverse
from Icesi_Students_Management.models import Actividad
from Icesi_Students_Management.models import Student
from Icesi_Students_Management.models import Beca
from Icesi_Students_Management.forms import ActivityForm

# Create your tests here.
class registroActividadTestCase(TestCase):

    
        

    def test_creacion_actividad(self):
        beca = Beca.objects.create(id = 1, type = 'Completa', description = 'Ejemplo')
        estudiante = Student.objects.create(id= 1, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id=1)

        activity = Actividad.objects.create(student =  estudiante,name = 'Natación',assists = 4)
        self.assertEquals(activity.name,'Natación')
        self.assertEqual(activity.assists,4)

    def test_vista_registrarActividad(self):
        response = self.client.get(reverse('registroActividades'))
        print(response)
        self.assertEquals(response.status_code,200)

    def test_valid_Activity_form(self):
        beca = Beca.objects.create(id = 1, type = 'Completa', description = 'Ejemplo')
        estudiante = Student.objects.create(id= 1, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id=1)
        data = {
            'student':estudiante,
            'name': 'Voley',
            'assists': 6
        }
        form = ActivityForm(data=data)
        
        self.assertTrue(form.is_valid())

