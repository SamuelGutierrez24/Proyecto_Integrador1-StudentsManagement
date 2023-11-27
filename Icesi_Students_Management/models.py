from django.db import models
from django.contrib.auth.models import AbstractUser

class Carrera(models.Model):
    nameCarrera = models.CharField(max_length=50)
    carreraID = models.CharField(primary_key=True, max_length=15)
    precioMatricula = models.DecimalField(max_digits=30, decimal_places=2, default=0.0)
    def str(self):
        return self.name

class Becas(models.Model):
    type = models.CharField(max_length=30)
    percentage = models.IntegerField(default=None)
    description = models.TextField(blank=True)
    alimentacion = models.BooleanField(default=None)
    transporte = models.BooleanField(default=None)

    def str(self):
        return self.type

class Student(models.Model):
    id = models.IntegerField(
        primary_key=True, auto_created=True, serialize=True, unique=True
    )
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    code = models.CharField(max_length=15, unique=True)
    email = models.CharField(max_length=40)
    beca = models.ForeignKey(
        Becas, related_name="BecaType", on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.code

class Materia(models.Model):
    materia_code = models.CharField(max_length=20, default="None")
    nombre = models.CharField(max_length=20, default="None")
    creditos =models.PositiveIntegerField(default=0)
    def str(self):
        return self.nombre

class Status(models.Model):
    StatusID = models.AutoField(primary_key=True, default=None)
    STATUS_CHOICES = (
        ('Materia Cancelada', 'Materia Cancelada'),
        ('Materia en Curso', 'Materia en Curso'),
        ('Materia completada', 'Materia completada'),
    )
    type = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def str(self):
        return self.type

class Semester(models.Model):
    SEMESTER_CHOICES = [
        ('Primer Semestre', '2023-1'),
        ('Segundo Semestre', '2022-2'),
        ('Tercer Semestre', '2022-1'),
        ('Cuarto Semestre', '2021-2'),
        ('Quinto Semestre', '2021-1'),
        ('Sexto Semestre', '2020-2'),
        ('Septimo Semestre', '2020-1'),
        ('Octavo Semestre', '2019-2'),
        ('Noveno Semestre', '2019-1'),
        ('Decimo Semestre', '2018-2'),
        ('Onceavo Semestre', '2018-1'),
        ('Doceavo Semestre', '2017-2'),
    ]
    name = models.CharField(max_length=200, choices=SEMESTER_CHOICES)
    def __str__(self):
        return self.name

class SeguimientoBeca(models.Model):
    testimonio = models.CharField(max_length=100, default="")
    studentID = models.ForeignKey(
        Student, on_delete=models.CASCADE, default=None)
    SemesterID = models.ForeignKey(
        Semester, on_delete=models.CASCADE, default=None)
    carreraID = models.ForeignKey(
        Carrera, on_delete=models.CASCADE, default=None)

class InformacionFinanciera(models.Model):
    informeID = models.AutoField(primary_key=True)
    studentID = models.CharField(max_length=15, default='')

    type = models.CharField(max_length=20, default='')
    # Gasto almuerzo: -10.000$ Fecha: 12/02/23
    dineroAsignado = models.DecimalField(max_digits=30, decimal_places=2)

    matriculaBeca = models.DecimalField(
        max_digits=30, decimal_places=2, default=0.0)
    transporteBeca = models.DecimalField(
        max_digits=30, decimal_places=2, default=0.0)
    alimentacionBeca = models.DecimalField(
        max_digits=30, decimal_places=2, default=0.0)
    gasto = models.DecimalField(max_digits=30, decimal_places=2, default=0.0)
    fecha = models.DateField()
    seguimientoBecaID = models.ForeignKey(
        SeguimientoBeca, on_delete=models.CASCADE, default=None)
    def str(self):
        return self.studentID

class HistorialGastos(models.Model):
    informacion_financiera = models.ForeignKey(
        InformacionFinanciera, on_delete=models.CASCADE)

    descripcion = models.CharField(max_length=255)
    fecha = models.DateField(auto_now_add=True)
    comprobantePago = models.FileField(upload_to='uploads/', null=True, blank=True)

    def _str_(self):
        return self.descripcion

class Actividad(models.Model):
    nombre = models.CharField(max_length=35, unique=True)
    
    class Tipo(models.IntegerChoices):
        TNULL = 0, ('None')
        BU = 1,('Actividad Bienestar')
        CR = 2, ('Actividad CREA')

    tipo = models.IntegerField(default=Tipo.TNULL,choices=Tipo.choices)
    def __str__(self):
        return self.nombre

class AsistenciasActividad(models.Model):
    seguimientoID = models.ForeignKey(SeguimientoBeca,on_delete=models.CASCADE,)
    ActividadID = models.ForeignKey(Actividad,on_delete=models.CASCADE)

    def __str__(self):
        return self.ActividadID.nombre

class BalanceAcademico(models.Model):
    BalanceAcademicoID = models.AutoField(primary_key=True, default=None)
    statusID = models.ForeignKey(Status, on_delete=models.CASCADE, default=None)
    materiaID = models.ForeignKey(Materia, on_delete=models.CASCADE, default=None)
    SeguimientoBecaID = models.ForeignKey(SeguimientoBeca, on_delete=models.CASCADE, default=None)

class Nota(models.Model):
    BalanceAcademicoID = models.ForeignKey(BalanceAcademico, on_delete=models.CASCADE, default=None)
    notaFinal = models.FloatField(default=0.0)

class Donante(models.Model):
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    typeBecas = models.ForeignKey(Becas, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.name
    
class User(AbstractUser):
    userID = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    class Role(models.IntegerChoices):
        RNULL = 0, ('None')
        ADMIN = 1,('Administrador')
        FILANTROPIA = 2, ('Filantropia')
        BU = 3, ('Bienestar Universitario')
        CONTABILIDAD = 4, ('Contabilidad')
        DIRECTOR = 5, ('Director del programa')
        CREA = 6, ('Usuario del CREA')

    rol = models.IntegerField(default=Role.RNULL,choices=Role.choices)

class Alerta(models.Model):
    title = models.CharField(max_length=40,default='Notificación')
    class Type_alert(models.IntegerChoices):
        NNULL = 0, ('None')
        ACTUALIZE_CONTA = 1, ('Oficina de Contabilidad')
        ACTUALIZE_BU = 2, ('Oficina de Bienestar Universitario')
        ACTUALIZE_DIRECTOR = 3, ('Oficina de Balance Academico')
        FILANTROPIA =  4,('Oficina de Filantropía')
        CREA = 5, ('Oficina de CREA')

    type = models.IntegerField(default=Type_alert.NNULL, choices=Type_alert.choices)
    description = models.TextField(blank=True)
    StudentID = models.ForeignKey(Student, on_delete=models.CASCADE, default=None, null=True, blank=True)
    isRead = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    def strBA(self):
        return (self.title + " | " + self.description)

class AsistenciaCREA(models.Model):
    activity= models.ForeignKey(Actividad,on_delete=models.CASCADE,default=None)
    seguimiento = models.ForeignKey(SeguimientoBeca, on_delete=models.CASCADE, default=None)
    reason = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.activity.nombre
    
class HistoryActivityAssistance(models.Model):
    date = models.DateField(auto_now=True)
    student = models.ForeignKey(Student,on_delete=models.CASCADE,default=None)
    activity = models.ForeignKey(Actividad, on_delete=models.CASCADE,default=None)
    
    def __str__(self):
        return "Cambios en:" + self.student.name



