# Generated by Django 4.2.5 on 2023-11-27 03:36

from django.db import migrations
from ..models import *
from datetime import datetime
from django.contrib.auth.hashers import make_password

class Migration(migrations.Migration):
    
    dependencies = [
        ('Icesi_Students_Management', '0001_initial'),
    ]
    
    def insert_default_values(apps, schema_editor):
        
        usersValues = [
            ["1", "Administrador", "ADMIN", "Administrador@gmail.com", "3178959649", "A", "Admin"],
            ["2", "Filantropia", "FILA", "Filantropia@gmail.com", "3178959642", "F", "Fila"],
            ["3", "Bienestar Universitario", "BIENESTAR", "BienestarUniversitario@gmail.com", "3178959679", "B", "Bienestar"],
            ["4", "Contabilidad", "CONTA", "Contabilidad@gmail.com", "31789549475", "C", "Conta"],
            ["5", "Director del programa", "DIRECTOR", "DirectorPrograma@gmail.com", "31789549410", "D", "Director"],
            ["6", "Usuario del CREA", "CREA", "Crea@gmail.com", "31489549410", "U", "Crea"]
        ]
        
        for user in usersValues:
            if user[0] == "1":
                User(first_name = user[1], password = make_password(user[2]), email = user[3], is_active = True, is_staff = False, is_superuser = False, phone = user[4], last_name = user[5], username = user[6], rol = 1).save()
            elif user[0] == "2":
                User(first_name = user[1], password = make_password(user[2]), email = user[3], is_active = True, is_staff = False, is_superuser = False, phone = user[4], last_name = user[5], username = user[6], rol = 2).save()
            elif user[0] == "3":
                User(first_name = user[1], password = make_password(user[2]), email = user[3], is_active = True, is_staff = False, is_superuser = False, phone = user[4], last_name = user[5], username = user[6], rol = 3).save()
            elif user[0] == "4":
                User(first_name = user[1], password = make_password(user[2]), email = user[3], is_active = True, is_staff = False, is_superuser = False, phone = user[4], last_name = user[5], username = user[6], rol = 4).save()
            elif user[0] == "5":
                User(first_name = user[1], password = make_password(user[2]), email = user[3], is_active = True, is_staff = False, is_superuser = False, phone = user[4], last_name = user[5], username = user[6], rol = 5).save()
            elif user[0] == "6":
                User(first_name = user[1], password = make_password(user[2]), email = user[3], is_active = True, is_staff = False, is_superuser = False, phone = user[4], last_name = user[5], username = user[6], rol = 6).save()
        
        beca1 = Becas(type = "Completa", percentage = "100", description = "Aqui deberia de haber texto asi es", alimentacion = True,transporte = True)
        beca1.save()
        
        beca2 = Becas(type = " Semi completa", percentage = "50", description = "Aqui deberia de haber texto asi es", alimentacion = False,transporte = True)
        beca2.save()
        
        beca3 = Becas(type = " Semi", percentage = "25", description = "Aqui deberia de haber texto asi es", alimentacion = False,transporte = False)
        beca3.save()
        
        Donante1 = Donante(name = "Anibal", lastName = "Sosa", email = "AnibalSosa@gmail.com", typeBecas = beca1)
        Donante1.save()
        
        Donante2 = Donante(name = "Domiciano", lastName = "Rincon", email = "DomicianoRincon@gmail.com", typeBecas = beca2)
        Donante2.save()
        
        Donante3 = Donante(name = "Andres", lastName = "Aristizabal", email = "AndresAristizabal@gmail.com", typeBecas = beca3)
        Donante3.save()
        
        Student1 = Student(id = 0, name = "Luis", lastName = "Pinillos", code = "A00892312", email = "LuisPinillos@gmail.com", beca = beca1)
        Student1.save()
        
        Student2 = Student(id = 1, name = "Kevin", lastName = "Loachamin", code = "A00312897", email = "KevinLoachamin@gmail.com", beca = beca2)
        Student2.save()
        
        Student3 = Student(id = 2, name = "Daniel", lastName = "Vacaflor", code = "A00873451", email = "DanielVacaflor@gmail.com", beca = beca3)
        Student3.save()
        
        Carrera1 = Carrera(nameCarrera = "Ingenieria de Sistemas", carreraID = "SIS-007", precioMatricula = 12730000)
        Carrera1.save()
        
        Carrera2 = Carrera(nameCarrera = "Ingenieria Telematica", carreraID = "TEL-004", precioMatricula = 12730000)
        Carrera2.save()
        
        Carrera3 = Carrera(nameCarrera = "Administracion de Empresas", carreraID = "ADE-002", precioMatricula = 13340000)
        Carrera3.save()
        
        Semestre1 = Semester(name = "2020-1")
        Semestre1.save()
        
        Semestre2 = Semester(name = "2021-1")
        Semestre2.save()
        
        Semestre3 = Semester(name = "2022-1")
        Semestre3.save()
        
        SeguimientoBeca1 = SeguimientoBeca(testimonio = "Aqui deberia de haber texto asi es", studentID = Student1, SemesterID = Semestre1, carreraID = Carrera1)
        SeguimientoBeca1.save()
        
        SeguimientoBeca2 = SeguimientoBeca(testimonio = "Aqui deberia de haber texto asi es", studentID = Student2, SemesterID = Semestre2, carreraID = Carrera2)
        SeguimientoBeca2.save()
        
        SeguimientoBeca3 = SeguimientoBeca(testimonio = "Aqui deberia de haber texto asi es", studentID = Student3, SemesterID = Semestre3, carreraID = Carrera3)
        SeguimientoBeca3.save()
        
        #Informacion Financiera 1
        dineroTransporte1 = 0
        dineroAlimentacion1 = 0
        dineroMatricula1 = (float(Student1.beca.percentage)/100) * float(SeguimientoBeca1.carreraID.precioMatricula)
                
        dineroTotal1 = dineroMatricula1
        if Student1.beca.alimentacion:
            dineroTotal1 += 800000
            dineroAlimentacion1 += 800000
        if Student1.beca.transporte:
            dineroTotal1 += 432000
            dineroTransporte1 += 432000
        
        fecha = datetime(2023, 10, 14).date()
        
        InformacionFinanciera1 = InformacionFinanciera(studentID = Student1, type = beca1.type, dineroAsignado = dineroTotal1, matriculaBeca = dineroMatricula1, transporteBeca = dineroTransporte1, alimentacionBeca = dineroAlimentacion1, gasto = 0, fecha = fecha, seguimientoBecaID = SeguimientoBeca1)
        InformacionFinanciera1.save()
        
        #Informacion Financiera 2
        dineroTransporte2 = 0
        dineroAlimentacion2 = 0
        dineroMatricula2 = (float(Student2.beca.percentage)/100) * float(SeguimientoBeca2.carreraID.precioMatricula)
                
        dineroTotal2 = dineroMatricula2
        if Student2.beca.alimentacion:
            dineroTotal2 += 800000
            dineroAlimentacion2 += 800000
        if Student2.beca.transporte:
            dineroTotal2 += 432000
            dineroTransporte2 += 432000
        
        InformacionFinanciera2 = InformacionFinanciera(studentID = Student2, type = beca2.type, dineroAsignado = dineroTotal2, matriculaBeca = dineroMatricula2, transporteBeca = dineroTransporte2, alimentacionBeca = dineroAlimentacion2, gasto = 0, fecha = fecha, seguimientoBecaID = SeguimientoBeca2)
        InformacionFinanciera2.save()
        
        #Informacion Financiera 3
        dineroTransporte3 = 0
        dineroAlimentacion3 = 0
        dineroMatricula3 = (float(Student3.beca.percentage)/100) * float(SeguimientoBeca3.carreraID.precioMatricula)
                
        dineroTotal3 = dineroMatricula3
        if Student3.beca.alimentacion:
            dineroTotal3 += 800000
            dineroAlimentacion3 += 800000
        if Student3.beca.transporte:
            dineroTotal3 += 432000
            dineroTransporte3 += 432000
        
        InformacionFinanciera3 = InformacionFinanciera(studentID = Student3, type = beca3.type, dineroAsignado = dineroTotal3, matriculaBeca = dineroMatricula3, transporteBeca = dineroTransporte3, alimentacionBeca = dineroAlimentacion3, gasto = 0, fecha = fecha, seguimientoBecaID = SeguimientoBeca3)
        InformacionFinanciera3.save()
        
        ActividadB1 = Actividad(nombre = "Danza Moderna", tipo = 1)
        ActividadB1.save()
        
        ActividadB2 = Actividad(nombre = "Futbol", tipo = 1)
        ActividadB2.save()
        
        ActividadB3 = Actividad(nombre = "Tenis de mesa", tipo = 1)
        ActividadB3.save()
        
        ActividadC1 = Actividad(nombre = "Taller de Artesanias", tipo = 2)
        ActividadC1.save()
        
        ActividadC2 = Actividad(nombre = "Taller de Dibujo", tipo = 2)
        ActividadC2.save()
        
        ActividadC3 = Actividad(nombre = "Taller de Origami", tipo = 2)
        ActividadC3.save()
    
    
    operations = [
        migrations.RunPython(insert_default_values),
    ]