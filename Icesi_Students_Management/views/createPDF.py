from ..models import Student
from django.shortcuts import render
from django.views.generic import View
from .utils import render_to_pdf
from django.http import HttpResponse

class seguimientoBecaPDF(View):
    def get(self, request, *args, **kwargs):
        estudiante = Student.objects.all()
        data = {
            'estudiante': estudiante
        }
        pdf = render_to_pdf('estiloSB.html', data)
        return HttpResponse(pdf, content_type='application/pdf')