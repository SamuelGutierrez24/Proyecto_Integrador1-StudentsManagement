# Generated by Django 4.2.5 on 2023-10-16 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icesi_Students_Management', '0002_historialgastos_comprobantepago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialgastos',
            name='comprobantePago',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
