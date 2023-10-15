# Generated by Django 4.2.5 on 2023-10-15 06:37

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Notificaci贸n', max_length=40)),
                ('type', models.IntegerField(choices=[(0, 'None'), (1, 'Actualizacion de informacion contabilidad'), (2, 'Actualizacion de informacion Bienestar Universitario'), (3, 'Actualizacion de informacion Director de programa'), (4, 'Actualizaci贸n de actividades no academicas de un estudiante')], default=0)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='BalanceAcademico',
            fields=[
                ('BalanceAcademicoID', models.AutoField(default=None, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Becas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('percentage', models.IntegerField(default=None)),
                ('description', models.TextField(blank=True)),
                ('alimentacion', models.BooleanField(default=None)),
                ('transporte', models.BooleanField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('nameCarrera', models.CharField(max_length=50)),
                ('carreraID', models.CharField(default='0', max_length=15, primary_key=True, serialize=False)),
                ('precioMatricula', models.DecimalField(decimal_places=2, default=0.0, max_digits=30)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia_code', models.CharField(default='None', max_length=20)),
                ('nombre', models.CharField(default='None', max_length=20)),
                ('creditos', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('StatusID', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('Materia Cancelada', 'Materia Cancelada'), ('Materia en Curso', 'Materia en Curso'), ('Materia completada', 'Materia completada')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('userID', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=15)),
                ('rol', models.IntegerField(choices=[(0, 'None'), (1, 'Administrador'), (2, 'Filantropia'), (3, 'Bienestar Universitario'), (4, 'Contabilidad'), (5, 'Director del programa')], default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(auto_created=True, default=0, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=15, unique=True)),
                ('email', models.CharField(max_length=40)),
                ('beca', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='BecaType', to='Icesi_Students_Management.becas')),
            ],
        ),
        migrations.CreateModel(
            name='SeguimientoBeca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonio', models.CharField(default='', max_length=100)),
                ('SemesterID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.semester')),
                ('studentID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.student')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notaFinal', models.FloatField(default=0.0)),
                ('BalanceAcademicoID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.balanceacademico')),
            ],
        ),
        migrations.CreateModel(
            name='InformacionFinanciera',
            fields=[
                ('informeID', models.AutoField(primary_key=True, serialize=False)),
                ('studentID', models.CharField(default='', max_length=15)),
                ('type', models.CharField(choices=[('Alimentaci贸n', 'Alimientaci贸n'), ('Matricula', 'Matricula'), ('Transporte', 'Transporte')], max_length=20)),
                ('dineroAsignado', models.DecimalField(decimal_places=2, max_digits=30)),
                ('gasto', models.DecimalField(decimal_places=2, default=0.0, max_digits=30)),
                ('fecha', models.DateField()),
                ('seguimientoBecaID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.seguimientobeca')),
            ],
        ),
        migrations.CreateModel(
            name='Donante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('typeBecas', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.becas')),
            ],
        ),
        migrations.AddField(
            model_name='balanceacademico',
            name='SeguimientoBecaID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.seguimientobeca'),
        ),
        migrations.AddField(
            model_name='balanceacademico',
            name='materiaID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.materia'),
        ),
        migrations.AddField(
            model_name='balanceacademico',
            name='statusID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.status'),
        ),
        migrations.CreateModel(
            name='AsistenciasActividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ActividadID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.actividad')),
                ('seguimientoID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.seguimientobeca')),
            ],
        ),
    ]
