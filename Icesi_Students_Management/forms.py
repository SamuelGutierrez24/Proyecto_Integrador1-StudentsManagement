from django import forms
from .models import *
class DateInput(forms.DateInput):
    input_type = 'date'


class registrarInfoFinanciera(forms.ModelForm):

    CATEGORIA_CHOICES = [
        ('matricula', 'Matrícula'),
        ('transporte', 'Transporte'),
        ('alimentacion', 'Alimentación'),
    ]

    categoriaGasto = forms.ChoiceField(label='Categoría del Gasto', choices=CATEGORIA_CHOICES)

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
        fields = ['studentID', 'type', 'matriculaBeca','transporteBeca','alimentacionBeca','dineroAsignado', 'gasto','categoriaGasto']


class registrarInfoFinancieraModificar(forms.ModelForm):

    CATEGORIA_CHOICES = [
        ('matricula', 'Matrícula'),
        ('transporte', 'Transporte'),
        ('alimentacion', 'Alimentación'),
    ]

    categoriaGasto = forms.ChoiceField(label='Categoría del Gasto', choices=CATEGORIA_CHOICES)


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
        fields = ['studentID', 'type', 'matriculaBeca','transporteBeca','alimentacionBeca','dineroAsignado', 'gasto','categoriaGasto']


class HistorialGastosForm(forms.ModelForm):
    comprobantePago = forms.FileField(label="Comprobante de Pago", required=False)
    class Meta:
        model = HistorialGastos
        fields = ['comprobantePago']
