from django.db import models
from django.contrib.auth.models import AbstractUser



class Carrera(models.Model):
    nameCarrera = models.CharField(max_length=50)
    carreraID = models.CharField(primary_key=True, max_length=15, default="0")
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
        primary_key=True,auto_created=True,serialize=True,unique=True, default=0
    )
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    code = models.CharField(max_length=15,unique=True)
    email = models.CharField(max_length=40)
    beca = models.ForeignKey(Becas, related_name="BecaType", on_delete= models.CASCADE, default= None)
    def __str__(self):
        return self.code


class Materia(models.Model):
    materia_code = models.CharField(max_length=20, default="None")
    nombre = models.CharField(max_length=20, default="None")
    creditos =models.PositiveIntegerField(default=0)
    def str(self):
        return self.nombre



class Status(models.Model):
    STATUS_CHOICES = (
        ('Materia Cancelada', 'Materia Cancelada'),
        ('Materia en Curso', 'Materia en Curso'),
        ('Materia completada', 'Materia completada'),
    )
    type = models.CharField(max_length=20, choices=STATUS_CHOICES)
    def str(self):
        return self.type

class Semester(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class SeguimientoBeca(models.Model):
    testimonio = models.CharField(max_length=100, default= "")
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)
    SemesterID = models.ForeignKey(Semester,on_delete=models.CASCADE,default=None)


class InformacionFinanciera(models.Model):
    informeID = models.AutoField(primary_key=True)
    studentID = models.CharField(max_length=15, default='')
    STATUS_CHOICES = (
        ('Alimentación', 'Alimientación'),
        ('Matricula', 'Matricula'),
        ('Transporte', 'Transporte'),
    )
    type = models.CharField(max_length=20, choices=STATUS_CHOICES)

    dineroAsignado = models.DecimalField(max_digits=30, decimal_places=2)
    gasto = models.DecimalField(max_digits=30, decimal_places=2, default=0.0)
    fecha = models.DateField()
    seguimientoBecaID = models.ForeignKey(SeguimientoBeca, on_delete=models.CASCADE, default=None)

    def str(self):
        return self.studentID

class Actividad(models.Model):
    nombre = models.CharField(max_length=35, unique=True)

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
    SeguimientoBecaID = models.ForeignKey(SeguimientoBeca, on_delete=models.CASCADE, default=None, null=True)

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

    rol = models.IntegerField(default=Role.RNULL,choices=Role.choices)
    


class Alerta(models.Model):
    title = models.CharField(max_length=40,default='Notificación')
    class Type_alert(models.IntegerChoices):
        NNULL = 0, ('None')
        ACTUALIZE_CONTA = 1, ('Actualizacion de informacion contabilidad')
        ACTUALIZE_BU = 2, ('Actualizacion de informacion Bienestar Universitario')
        ACTUALIZE_DIRECTOR = 3, ('Actualizacion de informacion Director de programa')
        FILANTROPIA =  4,('Actualización de actividades no academicas de un estudiante')


    type = models.IntegerField(default=Type_alert.NNULL, choices=Type_alert.choices)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.title

#class SeguimientoCREA(models.Model):
    #seguimientoCreaID = models.CharField(max_length=20)
    #userID = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    #def __str__(self):
      #  return self.seguimientoCreaID


#class Consulta(models.Model):
   # consultaID = models.CharField(max_length=20)
    #date = models.DateField()
    #hour = models.TimeField()
    #reason = models.CharField(max_length=50)
    #result = models.CharField(max_length=20)
    #seguimientoCreaID = models.ForeignKey(SeguimientoCREA, on_delete=models.CASCADE, default=None)
    #def __str__(self):
       #return self.consultaID


    def __str__(self):
        return self.reporteBecaID
