# Generated by Django 4.2.5 on 2023-11-27 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icesi_Students_Management', '0007_merge_0005_alter_alerta_type_0006_alter_alerta_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='semester',
            name='name',
            field=models.CharField(choices=[('Primer Semestre', '2023-1'), ('Segundo Semestre', '2022-2'), ('Tercer Semestre', '2022-1'), ('Cuarto Semestre', '2021-2'), ('Quinto Semestre', '2021-1'), ('Sexto Semestre', '2020-2'), ('Septimo Semestre', '2020-1'), ('Octavo Semestre', '2019-2'), ('Noveno Semestre', '2019-1'), ('Decimo Semestre', '2018-2'), ('Onceavo Semestre', '2018-1'), ('Doceavo Semestre', '2017-2')], max_length=200),
        ),
    ]