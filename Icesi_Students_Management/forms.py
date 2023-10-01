from django.forms import ModelForm
from django import forms
from .models import Actividad

class ActivityForm(ModelForm):

    student = forms.CharField(
        label='Codigo de estudiante', max_length=9, widget=forms.TextInput(attrs={"class":"input"})
    )
    name = forms.CharField(
        label='Nombre de la actividad', max_length=20,widget=forms.TextInput(attrs={"class":"input"})
    )
    
    assists = forms.CharField(
        label='Asistencias'
    )

    class Meta:
        model = Actividad
        fields = ['student', 'name', 'assists']
