from .models import Materia
from django.forms import ModelForm
from django import forms
from .models import Actividad
from .models import AsistenciasActividad
from .models import AsistenciaCREA
from .models import *
from django.forms import Form


class RegNotasBAForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['materia_code', 'nombre', 'creditos']

class CreaForm(ModelForm):

    student = forms.CharField(
        label='Codigo del estudiante', max_length=9, widget=forms.TextInput(attrs={"class":"input"},)
    )

    activity = forms.ModelChoiceField(
        queryset=Actividad.objects.all().filter(tipo=2),  # Esto recupera todas las actividades de la base de datos
        label='Selecciona una actividad',
        empty_label='Selecciona una actividad',  # Etiqueta para la opción vacía
        widget=forms.Select(attrs={"class": "input"})  # Utiliza un widget de selección
    )
    reason = forms.CharField(
        label='Motivo',
        max_length=50,  # Elige una longitud máxima adecuada
        widget=forms.Textarea(attrs={"class": "input"})
    )

    class Meta:
        model = AsistenciaCREA
        fields = ['student', 'activity', 'reason']

class ActivityForm(ModelForm):

    student = forms.CharField(
        label= 'Codigo de estudiante', max_length=9, widget=forms.TextInput(attrs={"class":"input"},)
    )

    activity = forms.ModelChoiceField(
        queryset=Actividad.objects.all().filter(tipo=1),  # Esto recupera todas las actividades de la base de datos

        label='Selecciona una actividad',
        empty_label='Selecciona una actividad',  # Etiqueta para la opción vacía
        # Utiliza un widget de selección
        widget=forms.Select(attrs={"class": "input"})
    )

    class Meta:
        model = AsistenciasActividad
        fields = ['student', 'activity']


class DateInput(forms.DateInput):
    input_type = 'date'


class registrarInfoFinanciera(forms.ModelForm):

    CATEGORIA_CHOICES = [
        ('matricula', 'Matrícula'),
        ('transporte', 'Transporte'),
        ('alimentacion', 'Alimentación'),
    ]

    categoriaGasto = forms.ChoiceField(
        label='Categoría del Gasto', choices=CATEGORIA_CHOICES)

    studentID = forms.CharField(
        label="Codigo Estudiante",
        max_length=20,
        required=False
    )
    type = forms.CharField(label="Tipo de beca",
                           max_length=20,
                           widget=forms.HiddenInput())

    matriculaBeca = forms.DecimalField(label="Dinero para la matricula",
                                       max_digits=10,
                                       decimal_places=2,
                                       widget=forms.HiddenInput())

    transporteBeca = forms.DecimalField(label="Dinero para el transporte",
                                        max_digits=10,
                                        decimal_places=2,
                                        widget=forms.HiddenInput())

    alimentacionBeca = forms.DecimalField(label="Dinero para la alimentación",
                                          max_digits=10,
                                          decimal_places=2,
                                          widget=forms.HiddenInput())

    dineroAsignado = forms.DecimalField(label="Dinero total de la beca",
                                        max_digits=10,
                                        decimal_places=2,
                                        widget=forms.HiddenInput())

    gasto = forms.DecimalField(label="Gasto a registrar",
                               max_digits=10,
                               decimal_places=2)
    fecha = forms.DateField(label="Fecha",
                            widget=DateInput)

    class Meta:
        model = InformacionFinanciera
        widgets = {'fecha': DateInput()}
        fields = ['studentID', 'type', 'matriculaBeca', 'transporteBeca',
                  'alimentacionBeca', 'dineroAsignado', 'gasto', 'categoriaGasto']


class registrarInfoFinancieraModificar(forms.ModelForm):

    CATEGORIA_CHOICES = [
        ('matricula', 'Matrícula'),
        ('transporte', 'Transporte'),
        ('alimentacion', 'Alimentación'),
    ]

    categoriaGasto = forms.ChoiceField(
        label='Categoría del Gasto', choices=CATEGORIA_CHOICES)

    studentID = forms.CharField(
        label="Codigo Estudiante",
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    type = forms.CharField(label="Tipo de beca",
                           max_length=20,
                           widget=forms.HiddenInput())

    matriculaBeca = forms.DecimalField(label="Dinero para la matricula",
                                       max_digits=10,
                                       decimal_places=2,
                                       widget=forms.HiddenInput())

    transporteBeca = forms.DecimalField(label="Dinero para el transporte",
                                        max_digits=10,
                                        decimal_places=2,
                                        widget=forms.HiddenInput())

    alimentacionBeca = forms.DecimalField(label="Dinero para la alimentación",
                                          max_digits=10,
                                          decimal_places=2,
                                          widget=forms.HiddenInput())

    dineroAsignado = forms.DecimalField(label="Dinero Asignado al Estudiante",
                                        max_digits=10,
                                        decimal_places=2,
                                        widget=forms.HiddenInput())

    gasto = forms.DecimalField(label="Cantidad de gasto que se va a registrar",
                               max_digits=10,
                               decimal_places=2)
    fecha = forms.DateField(label="Fecha",
                            widget=DateInput)

    class Meta:
        model = InformacionFinanciera
        widgets = {'fecha': DateInput()}
        fields = ['studentID', 'type', 'matriculaBeca', 'transporteBeca',
                  'alimentacionBeca', 'dineroAsignado', 'gasto', 'categoriaGasto']


class HistorialGastosForm(forms.ModelForm):
    comprobantePago = forms.FileField(
        label="Comprobante de Pago", required=False)

    class Meta:
        model = HistorialGastos
        fields = ['comprobantePago']


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

class envioMensaje(forms.ModelForm):
    title = forms.CharField(label="Titulo", max_length=20, widget=forms.TextInput(attrs={'col': '10', 'size': '60'}))
    type = forms.ChoiceField(label="Destinatario", choices=Alerta.Type_alert.choices, widget=forms.Select)
    description = forms.CharField(label="Mensaje", max_length=20, required=False, widget=forms.Textarea(attrs={'col': '50', 'size': '80', 'rows': '8'}))

    class Meta:
        model = Alerta
        fields = ['title', 'type', 'description']

class modificarAlerta(forms.ModelForm):
    Title = forms.CharField(label="Titulo", widget=forms.TextInput(attrs={'col': '10', 'size': '60'}))
    Type = forms.ChoiceField(label="Tipo", choices=Alerta.Type_alert.choices, widget=forms.Select)
    Description = forms.CharField(label="Descripcion", widget=forms.Textarea(attrs={'col': '50', 'size': '80', 'rows': '8'}))
    Email = forms.EmailField(label="Correo Donante", widget=forms.TextInput(attrs={'col': '10', 'size': '60'}))

    class Meta:
        model = Alerta
        fields = ['Title', 'Type', 'Description', 'Email']