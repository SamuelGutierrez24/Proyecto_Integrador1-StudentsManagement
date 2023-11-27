from django.shortcuts import render, redirect, get_object_or_404
from Icesi_Students_Management.models import SeguimientoBeca
from ..forms import TestimonyForm
from django.contrib import messages

def addTestimony(request, code):
    seguimiento_beca = get_object_or_404(SeguimientoBeca, studentID=code)

    if request.method == 'POST':
        form = TestimonyForm(request.POST)

        if form.is_valid():
            testimonio = form.cleaned_data['testimonio']
            seguimiento_beca.testimonio = testimonio
            seguimiento_beca.save()
            messages.success(request,"Testimonio agregado correctamente!")
            return redirect('/menu_filantropia/testimonio.html')

    else:
        form = TestimonyForm()

    return render(request, 'createTestimony.html', {'form': form, 'seguimiento_beca': seguimiento_beca})
