from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from django.forms import ModelForm
from django import forms
from .models import *

class searchDonator(Form):
    donator = forms.ModelChoiceField(label = "Name", queryset=Donante.objects.all(), initial=3, widget=forms.Select(attrs={"class":"input"}))

class addStudent(Form):
    Nombre = forms.CharField(label="Nombre:", max_length=100)
    Apellido = forms.CharField(label="Apellido:", max_length=100)
    Email = forms.CharField(label="Email:", max_length=200)
    Codgio = forms.CharField(label="Codigo", max_length=100)
    Beca = searchDonator
    
    class Meta:
        model = Student
        fields = ['Nombre', 'Apellido', 'Email', 'Codigo', 'Beca']