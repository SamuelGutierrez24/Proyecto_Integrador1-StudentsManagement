from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    code = models.CharField(max_length=15)
    email = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Semester(models.Model):
    semesterID = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    faculty = models.CharField(max_length=25)
    description = models.TextField(blank=True)
    studentCode = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Becas(models.Model):
    type = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    studentCode = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.type


class Donante(models.Model):
    donanteID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    typeBecas = models.ForeignKey(Becas, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class BalanceAcademico(models.Model):
    balanceAcademicoID = models.CharField(max_length=20)
    program = models.CharField(max_length=20)

    def __str__(self):
        return self.program


class Materia(models.Model):
    materiaID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    scheduale = models.DateTimeField(null=True)
    assists = models.PositiveIntegerField()
    balanceAcademicoID = models.ForeignKey(BalanceAcademico, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class Status(models.Model):
    STATUS_CHOICES = (
        ('Materia Cancelada', 'Materia Cancelada'),
        ('Materia en Curso', 'Materia en Curso'),
        ('Materia completada', 'Materia completada'),
    )
    type = models.CharField(max_length=20, choices=STATUS_CHOICES)
    materiaID = models.ForeignKey(Materia, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.type


class SeguimientoActividades(models.Model):
    seguimientoActividadesID = models.CharField(max_length=20)
    actividadID = models.CharField(max_length=20)

    def __str__(self):
        return self.actividadID


class Actividad(models.Model):
    actividadID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    assists = models.PositiveIntegerField()
    seguimientoActividadesID = models.ForeignKey(SeguimientoActividades, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class User(models.Model):
    userID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Alerta(models.Model):
    alertaID = models.CharField(max_length=20)
    type = models.CharField(max_length=50)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.alertaID


class Roles(models.Model):
    STATUS_CHOICES = (
        ('Filantropia', 'Filantropia'),
        ('Bienestar', 'Bienestar'),
        ('Contabilidad', 'Contabilidad'),
        ('Director de Programa', 'Director de Programa'),
    )
    type = models.CharField(max_length=20, choices=STATUS_CHOICES)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.type


class SeguimientoCREA(models.Model):
    seguimientoCreaID = models.CharField(max_length=20)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.seguimientoCreaID


class Consulta(models.Model):
    consultaID = models.CharField(max_length=20)
    date = models.DateField()
    hour = models.TimeField()
    reason = models.CharField(max_length=50)
    result = models.CharField(max_length=20)
    seguimientoCreaID = models.ForeignKey(SeguimientoCREA, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.consultaID


class InformacionFinanciera(models.Model):
    informeID = models.CharField(max_length=20)
    dineroAsignado = models.DecimalField(max_digits=10, decimal_places=2)
    dineroUsado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.informeID


class SeguimientoBeca(models.Model):
    reporteBecaID = models.CharField(max_length=20)
    testimonio = models.CharField(max_length=100)
    informacionFinancieraID = models.ForeignKey(InformacionFinanciera, on_delete=models.CASCADE, default=None)
    SeguimientoActividadesID = models.ForeignKey(SeguimientoActividades, on_delete=models.CASCADE, default=None)
    balanceAcademicoID = models.ForeignKey(BalanceAcademico, on_delete=models.CASCADE, default=None)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    studentCode = models.ForeignKey(Student, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.reporteBecaID
