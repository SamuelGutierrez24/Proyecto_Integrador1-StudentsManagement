# Generated by Django 4.2.5 on 2023-11-14 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Icesi_Students_Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerta',
            name='StudentID',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.student'),
        ),
    ]
