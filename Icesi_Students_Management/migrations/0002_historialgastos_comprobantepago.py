# Generated by Django 4.2.5 on 2023-10-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Icesi_Students_Management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historialgastos',
            name='comprobantePago',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]