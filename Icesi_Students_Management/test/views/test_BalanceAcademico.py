from django.test import TestCase
from Icesi_Students_Management.models import BalanceAcademico, Status, Materia, Nota, SeguimientoBeca, Student, Semester, Becas, Carrera
from django.urls import reverse

class BalanceAcademicoModelTestCase(TestCase):
  
  def test_creacion_de_balance_academico(self):
    statusPrueba = Status.objects.create(type = "Materia Cancelada")
    materiaPrueba = Materia.objects.create(materia_code = "123-Mat", nombre = "Matematicas Aplicadas", creditos = 4)
    semestrePrueba = Semester.objects.create(name = "5")
    becaPrueba = Becas.objects.create(type = "Alimentos", percentage = 100, description = "descTest", alimentacion = True, transporte = False)
    estudiantePrueba = Student.objects.create(id = 1, name = "Kevin", lastName = "Loachamin", code = "A00100001", email = "test@gmail.com", beca = becaPrueba)
    carreraPrueba = Carrera.objects.create(nameCarrera = "ing SIS", carreraID = "1", precioMatricula = 1.0)
    seguimientoPrueba = SeguimientoBeca.objects.create(testimonio = "Prueba", studentID = estudiantePrueba, SemesterID = semestrePrueba, carreraID = carreraPrueba)
    balanceAcademico = BalanceAcademico.objects.create(statusID = statusPrueba, materiaID = materiaPrueba, SeguimientoBecaID = seguimientoPrueba)
    
    self.assertEqual(balanceAcademico.statusID.type, "Materia Cancelada")
    self.assertEqual(balanceAcademico.materiaID.materia_code, "123-Mat")
    self.assertEqual(balanceAcademico.SeguimientoBecaID.testimonio, "Prueba")
    
  def test_creacion_de_status(self):
    status = Status.objects.create(type = "Materia Cancelada")
    
    self.assertEqual(status.type, "Materia Cancelada")
    
  def test_creacion_de_materia(self):
    materia = Materia.objects.create(materia_code = "123-Mat", nombre = "Matematicas Aplicadas", creditos = 4)
    
    self.assertEqual(materia.materia_code, "123-Mat")
    self.assertEqual(materia.nombre, "Matematicas Aplicadas")
    self.assertEqual(materia.creditos, 4)
    
  def test_creacion_de_nota(self):
    statusPrueba = Status.objects.create(type = "Materia Cancelada")
    materiaPrueba = Materia.objects.create(materia_code = "123-Mat", nombre = "Matematicas Aplicadas", creditos = 4)
    semestrePrueba = Semester.objects.create(name = "5")
    becaPrueba = Becas.objects.create(type = "Alimentos", percentage = 100, description = "descTest", alimentacion = True, transporte = False)
    estudiantePrueba = Student.objects.create(id = 2, name = "Kevin", lastName = "Loachamin", code = "A00100002", email = "test@gmail.com", beca = becaPrueba)
    carreraPrueba = Carrera.objects.create(nameCarrera = "ing SIS", carreraID = "2", precioMatricula = 1.0)
    seguimientoPrueba = SeguimientoBeca.objects.create(testimonio = "Prueba", studentID = estudiantePrueba, SemesterID = semestrePrueba, carreraID = carreraPrueba)
    balanceAcademico = BalanceAcademico.objects.create(statusID = statusPrueba, materiaID = materiaPrueba, SeguimientoBecaID = seguimientoPrueba)
    nota = Nota.objects.create(BalanceAcademicoID = balanceAcademico, notaFinal = 4.3)
    
    self.assertEqual(nota.BalanceAcademicoID.materiaID.materia_code, "123-Mat")
    self.assertEqual(nota.BalanceAcademicoID.materiaID.nombre, "Matematicas Aplicadas")
    self.assertEqual(nota.notaFinal, 4.3)


class VistaBalanceAcademicoTestCase(TestCase):

  def test_vista_menuBalanceAcademico(self):
    response = self.client.get(reverse('menuBalanceAcademico'))
    print(response)
    self.assertEqual(response.status_code, 200)
    
  def test_vista_buscarEstudiante(self):
    response = self.client.get(reverse('buscarEstudiante'))
    print(response)
    self.assertEqual(response.status_code, 200)
  
  def test_vista_registroNotas(self):
    # ----------------------------------------------------------------------- #
    # Variables necesarias para que la vista registroNotasBA pueda hacer la validacion inicial de la info del estudiante que llega por medio de estudData
    statusPrueba = Status.objects.create(type = "Materia Cancelada")
    materiaPrueba = Materia.objects.create(materia_code = "123-Mat", nombre = "Matematicas Aplicadas", creditos = 4)
    becaPrueba = Becas.objects.create(type = "Alimentos", percentage = 100, description = "descTest", alimentacion = True, transporte = False)
    estudiantePrueba = Student.objects.create(id = 3, name = "Kevin", lastName = "Loachamin", code = "A00100003", email = "test@gmail.com", beca = becaPrueba)
    semestrePrueba = Semester.objects.create(name = "5")
    carreraPrueba = Carrera.objects.create(nameCarrera = "ing SIS", carreraID = "3", precioMatricula = 1.0)
    seguimientoPrueba = SeguimientoBeca.objects.create(testimonio = "Prueba", studentID = estudiantePrueba, SemesterID = semestrePrueba, carreraID = carreraPrueba)
    balanceAcademicoPrueba = BalanceAcademico.objects.create(statusID = statusPrueba, materiaID = materiaPrueba, SeguimientoBecaID = seguimientoPrueba)
    notaPrueba = Nota.objects.create(BalanceAcademicoID = balanceAcademicoPrueba, notaFinal = 4.3)
    # ----------------------------------------------------------------------- #
    
    session = self.client.session
    session['estudData'] = {'nombre': 'Kevin', 'apellido': 'Loachamin', 'codigo': 'A00100003'}
    session.save()
    
    response = self.client.get(reverse('registroNotasBA'))
    print(response)
    self.assertEqual(response.status_code, 200)

class RegistroBalanceAcademicoTestCase(TestCase):
    def test_crear_registro(self):
        # Preparar los datos para la solicitud POST
        
        # ----------------------------------------------------------------------- #
        # Variables necesarias para que la vista registroNotasBA pueda hacer la validacion inicial de la info del estudiante que llega por medio de estudData
        becaPrueba = Becas.objects.create(type = "Alimentos", percentage = 100, description = "descTest", alimentacion = True, transporte = False)
        estudiantePrueba = Student.objects.create(id = 4, name = "Kevin", lastName = "Loachamin", code = "A00100004", email = "test@gmail.com", beca = becaPrueba)
        semestrePrueba = Semester.objects.create(name = "5")
        carreraPrueba = Carrera.objects.create(nameCarrera = "ing SIS", carreraID = "4", precioMatricula = 1.0)
        seguimientoPrueba = SeguimientoBeca.objects.create(testimonio = "Prueba", studentID = estudiantePrueba, SemesterID = semestrePrueba, carreraID = carreraPrueba)
        # ----------------------------------------------------------------------- #
        
        session = self.client.session
        session['estudData'] = {'nombre': 'Kevin', 'apellido': 'Loachamin', 'codigo': 'A00100004'}
        session.save()
        
        data = {
        'codMateria1': '123-Mat',
        'nombreMateria1': 'Matematicas Aplicadas',
        'creditosMateria1': 4,
        'estatusMateria1': 'Materia Cancelada',
        'Nota1': 4.3,
        }


        # Solicitud POST a la vista
        response = self.client.post(reverse('registroNotasBA'), data)

        self.assertEqual(response.status_code, 302)

        # Verificar que se creó un registro en la base de datos
        self.assertEqual(BalanceAcademico.objects.count(), 1)
        registro = BalanceAcademico.objects.first()
        self.assertEqual(registro.materiaID.materia_code, '123-Mat')
        self.assertEqual(registro.materiaID.nombre, 'Matematicas Aplicadas')
        self.assertEqual(registro.statusID.type, 'Materia Cancelada')