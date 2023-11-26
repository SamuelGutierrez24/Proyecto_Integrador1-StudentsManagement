from django.test import TestCase
from Icesi_Students_Management.models import *
from Icesi_Students_Management.forms import *
from django.urls import reverse

class VistaProductoTestCase(TestCase):

  def test_vista_notificacionEditable(self):
    beca = Becas.objects.create(type = 'Completa', percentage = '100', description='Beca completa', alimentacion= True, transporte = True)
    donante = Donante.objects.create(name = 'Kevin', lastName = 'Loachamin', email='Santiago.J.Belalcazar@gmail.com', typeBecas = beca)
    estudiante = Student.objects.create(id= 2, name = 'Luis', lastName = 'Pinillos', code = 'A00301045', email='luis@gmail.com', beca_id= '1')
    alerta = Alerta.objects.create(title = 'Notificacion', type = '4', description = 'Al estudiante le fue bien', StudentID = estudiante)

    response = self.client.get(reverse('envioAlerta', kwargs={'noti_id': '1'}))
    print(response)
    self.assertEqual(response.status_code, 200)

class FormsTestCase(TestCase):
    
  def test_valid_alert_form(self):

    data = {
      'Title': "Notificacion",
      'Type': 4,
      'Description': "Al estudiante le fue bien",
      'Email': "Santiago@gmail.com",
    }
    form = modificarAlerta(data=data)
    print(form.errors)
    self.assertTrue(form.is_valid())