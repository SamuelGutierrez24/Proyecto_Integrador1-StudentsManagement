from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from django.forms import ModelForm
from django import forms
from .models import *


class addStudent(forms.Form):
    Nombre = forms.CharField(label="Nombre:",
                            max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Ingrese el nombre del estudiante', 'col': '10', 'size': '50'}))
    Apellido = forms.CharField(label="Apellido:",
                               max_length=100,
                               widget=forms.TextInput(attrs={'placeholder': 'Ingrese el apellido del estudiante', 'col': '10', 'size': '50'}))
    Email = forms.EmailField(label="Email:",
                            max_length=200,
                            widget=forms.TextInput(attrs={'placeholder': 'Ingrese el email del estudiante', 'col': '10', 'size': '50'}))
    Codigo = forms.CharField(label="Codigo:",
                            max_length=100,
                            widget=forms.TextInput(attrs={'placeholder': 'Ingrese el codigo del estudiante', 'col': '10', 'size': '50'}))
    
    class Meta:
        model = Student
        fields = ['Nombre', 'Apellido', 'Email', 'Codigo']