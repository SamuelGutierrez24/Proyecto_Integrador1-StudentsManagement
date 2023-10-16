from django.db import models

class Becas(models.Model):
    type = models.CharField(max_length=30)
    percentage = models.IntegerField(default=None)
    description = models.TextField(blank=True)
    alimentacion = models.BooleanField(default=None)
    transporte = models.BooleanField(default=None)
    def __str__(self):
        return self.type

class Student(models.Model):
    id = models.IntegerField(
        primary_key=True,auto_created=True,serialize=True,unique=True
    )
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    code = models.CharField(max_length=15,unique=True)
    email = models.CharField(max_length=40)
    beca = models.ForeignKey(Becas, related_name="BecaType", on_delete= models.CASCADE, default= None)
    def __str__(self):
        return self.code

class Donante(models.Model):
    donanteID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    typeBecas = models.ForeignKey(Becas, on_delete=models.CASCADE, default=None)
    def __str__(self):
        return self.name

class User(models.Model):
    userID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.name

class Alerta(models.Model):

    title = models.CharField(max_length=40,default='Notification')
    class Type_alert(models.IntegerChoices):
        SOLICITUD = 0, ('Solicitud de informacion')
        UPLOAD = 1, ('Subida de informacion')
        NONE = 2, ('ningun tipo')
    
    type = models.IntegerField(default=Type_alert.NONE, choices=Type_alert.choices)
    description = models.TextField(blank=True)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    #def __str__(self):
        #return self.alertaID

