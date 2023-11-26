from django.test import TestCase
from Icesi_Students_Management.models import *
from Icesi_Students_Management.forms import *
from django.urls import reverse

class ProductoModelTestCase(TestCase):
  def test_creacion_de_beca(self):
    beca = Becas.objects.create(type = "Completa", percentage = "10", description = "Aqui deberia de haber texto asi es", alimentacion = True,transporte = True)
    self.assertEqual(beca.type, "Completa")
    self.assertEqual(beca.percentage, "10")
    self.assertEqual(beca.description, "Aqui deberia de haber texto asi es")
    self.assertEqual(beca.alimentacion, True)
    self.assertEqual(beca.transporte, True)
    
  def test_creacion_de_estudiante(self):
    beca = Becas.objects.create(type = "Completa", percentage = "10", description = "Aqui deberia de haber texto asi es", alimentacion = True,transporte = True)
    estudiante = Student.objects.create(id= 1, name="Luis", lastName="Pinillos", email="SanaYMomoMayorMina@gmail.com", code="A0023142", beca= beca)
    self.assertEqual(estudiante.id, 1)
    self.assertEqual(estudiante.name, "Luis")
    self.assertEqual(estudiante.lastName, "Pinillos")
    self.assertEqual(estudiante.email, "SanaYMomoMayorMina@gmail.com")
    self.assertEqual(estudiante.code, "A0023142")
    self.assertEqual(estudiante.beca, beca)


class VistaProductoTestCase(TestCase):

  def test_vista_menu_filantropia(self):
    response = self.client.get(reverse('menu filantropia'))
    print(response)
    self.assertEqual(response.status_code, 200)
    
  def test_vista_agregar_estudiante(self):
    response = self.client.get(reverse('agregar estudiante'))
    print(response)
    self.assertEqual(response.status_code, 200)
  
  def test_vista_agregar_estudiante2(self):
    response = self.client.get(reverse('agregar estudiante 2'))
    print(response)
    self.assertEqual(response.status_code, 200)
  
  def test_vista_agregar_estudiante3(self):
    response = self.client.get(reverse('agregar estudiante 3'))
    print(response)
    self.assertEqual(response.status_code, 200)

class FormsTestCase(TestCase):
    
  def test_valid_student_form(self):
    data = {
      'Nombre': 'Luis',
      'Apellido': 'Pinillos',
      'Email': 'SanaYMomoMayorMina@gmail.com',
      'Codigo': 'A0023142',
    }
    form = addStudent(data=data)
    self.assertTrue(form.is_valid())