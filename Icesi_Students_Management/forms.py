from django import forms
from .models import *

class registrarInfoFinanciera(forms.Form):
    studentID = forms.CharField(label="Código de Estudiante", max_length=20, required=False)
    studentName = forms.CharField(label="Nombre del Estudiante", max_length=20)
    dineroAsignado = forms.DecimalField(label="Dinero Asignado al Estudiante", max_digits=10, decimal_places=2)
    dineroUsado = forms.DecimalField(label="Dinero Usado por el Estudiante", max_digits=10, decimal_places=2)
    financialNote = forms.CharField(label="Nota financiera", widget=forms.Textarea)
    extraInfo = forms.CharField(label="Información extra", widget=forms.Textarea)

    class Meta:
        model = InformacionFinanciera
        fields = ['studentID','studentName','dineroAsignado','dineroUsado','financialNote','extraInfo']

