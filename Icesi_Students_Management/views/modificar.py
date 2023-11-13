from django.shortcuts import render, redirect, get_object_or_404
from Icesi_Students_Management.models import *
from ..forms import registrarInfoFinanciera, registrarInfoFinancieraModificar
from django.contrib import messages
from django.urls import reverse

def modificarInfo(request, code):
    tieneInfo = InformacionFinanciera.objects.filter(
        studentID=code).exists()

    if tieneInfo:
        estudiante = get_object_or_404(InformacionFinanciera, studentID=code)
        historial = HistorialGastos.objects.filter(informacion_financiera=estudiante).order_by('-id')
        
        data = {
            'form': registrarInfoFinancieraModificar(instance=estudiante),
            'tieneInfo': tieneInfo,
            'historial': historial
        }

        if request.method == 'POST':
            categoriaGasto = request.POST['categoriaGasto']
            formulario = registrarInfoFinancieraModificar(
                data=request.POST, instance=estudiante, files=request.FILES)
            
            if formulario.is_valid():
                instancia = formulario.save(commit=False)

                dineroAsignadoAnterior = estudiante.dineroAsignado
                gastoAnterior = estudiante.gasto
                diferenciaGasto = dineroAsignadoAnterior - gastoAnterior

                dineroMatricula = estudiante.matriculaBeca
                dineroTransporte = estudiante.transporteBeca
                dineroAlimentacion = estudiante.alimentacionBeca

                if categoriaGasto == "matricula":
                    diferenciaMatricula = dineroMatricula - gastoAnterior
                    diferenciaTransporte = estudiante.transporteBeca
                    diferenciaAlimentacion = estudiante.alimentacionBeca
                elif categoriaGasto == "transporte":
                    diferenciaMatricula = estudiante.matriculaBeca
                    diferenciaTransporte = dineroTransporte - gastoAnterior
                    diferenciaAlimentacion = estudiante.alimentacionBeca
                else:
                    diferenciaMatricula = estudiante.matriculaBeca
                    diferenciaTransporte = estudiante.transporteBeca
                    diferenciaAlimentacion = dineroAlimentacion - gastoAnterior

                if diferenciaMatricula < 0 or diferenciaAlimentacion < 0 or diferenciaTransporte < 0:
                    instancia.save()
                    messages.error(request, 'No hay fondos suficientes')
                else:
                    instancia.dineroAsignado = diferenciaGasto
                    instancia.alimentacionBeca = diferenciaAlimentacion
                    instancia.transporteBeca = diferenciaTransporte
                    instancia.matriculaBeca = diferenciaMatricula

                    descripcion = f"Gasto {request.POST['categoriaGasto']}: -{instancia.gasto} Fecha: {request.POST['fecha']}"
                    historialGasto = HistorialGastos(informacion_financiera=instancia, descripcion=descripcion)

                    comprobantePago = request.FILES.get('comprobantePago')
                    if comprobantePago:
                        historialGasto.comprobantePago = comprobantePago

                    historialGasto.save()

                    descripcionAlerta = f"Gasto {request.POST['categoriaGasto']}: -{instancia.gasto} Fecha: {request.POST['fecha']}"
                    titleAlerta = f"Nuevo gasto registrado para el estudiante con código: {code}"
                    typeAlerta = 4
                    alertaGenerada = Alerta(title=titleAlerta, type=typeAlerta, description=descripcionAlerta, StudentID = Student.objects.all().filter(code=code))
                    alertaGenerada.save()

                    instancia.gasto = 0
                    instancia.save()

                    messages.success(request, 'Gastos registrados correctamente!')
                    messages.success(request, 'Actualización enviada a filantropía!')
                    url = reverse('modificarInfo', args=[code])
                    return redirect(url)
            data["form"] = formulario
    else:
        messages.error(request, 'No se ha registrado la Información Financiera del estudiante')
        return redirect('/contabilidad/buscarEstud.html')
    
    return render(request, 'modificar.html', data)
