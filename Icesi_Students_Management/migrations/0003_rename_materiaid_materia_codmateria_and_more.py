# Generated by Django 4.2.5 on 2023-10-04 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Icesi_Students_Management', '0002_remove_alerta_alertaid_alerta_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materia',
            old_name='materiaID',
            new_name='codMateria',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='assists',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='balanceAcademicoID',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='name',
        ),
        migrations.RemoveField(
            model_name='materia',
            name='scheduale',
        ),
        migrations.AddField(
            model_name='materia',
            name='nota',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='materia',
            name='student',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Icesi_Students_Management.student'),
        ),
    ]
