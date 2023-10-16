from .models import Materia
from django.forms import ModelForm
from django import forms
from .models import Actividad
from .models import AsistenciasActividad

class RegNotasBAForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['materia_code', 'nombre', 'creditos']

class ActivityForm(ModelForm):

    student = forms.CharField(
        label='Codigo de estudiante', max_length=9, widget=forms.TextInput(attrs={"class":"input"})
    )

    activity = forms.ModelChoiceField(
        queryset=Actividad.objects.all(),  # Esto recupera todas las actividades de la base de datos
        label='Selecciona una actividad',
        empty_label='Selecciona una actividad',  # Etiqueta para la opción vacía
        widget=forms.Select(attrs={"class": "input"})  # Utiliza un widget de selección
    )
    

    class Meta:
        model = AsistenciasActividad
        fields = ['student', 'activity']
