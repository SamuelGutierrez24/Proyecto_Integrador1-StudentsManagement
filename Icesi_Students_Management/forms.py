from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form
from django.forms import ModelForm
from django import forms
from .models import *

class searchDonator(Form):
    donator = forms.ModelChoiceField(label = "Name", queryset=Donante.objects.all(), initial=3, widget=forms.Select(attrs={"class":"input"}))

#class addStudent(Form):