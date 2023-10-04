from django import forms
from .models import Materia

class RegNotasBAForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['student', 'codMateria', 'nota']