from django.shortcuts import render, redirect, get_object_or_404
from Icesi_Students_Management.models import *
from ..forms import registrarInfoFinanciera, registrarInfoFinancieraModificar
from django.contrib import messages


def modificarInfo(request, code):
    tiene_info = InformacionFinanciera.objects.filter(
        studentID=code).exists()

    if tiene_info:
        estudiante = get_object_or_404(InformacionFinanciera, studentID=code)
        historial = HistorialGastos.objects.filter(informacion_financiera=estudiante).order_by('-id')
        
        data = {
            'form': registrarInfoFinancieraModificar(instance=estudiante),
            'tiene_info': tiene_info,
            'historial': historial
        }

        if request.method == 'POST':
            categoriaGasto = request.POST['categoriaGasto']


            formulario = registrarInfoFinanciera(
                data=request.POST, instance=estudiante, files=request.FILES)
            
            if formulario.is_valid():
                instancia = formulario.save(commit=False)

                dinero_asignado_anterior = estudiante.dineroAsignado
                gasto_anterior = estudiante.gasto
                diferencia_gasto = dinero_asignado_anterior - gasto_anterior

                dineroMatricula = estudiante.matriculaBeca
                dineroTransporte = estudiante.transporteBeca
                dineroAlimentacion = estudiante.alimentacionBeca

                if categoriaGasto == "matricula":
                    diferenciaMatricula = dineroMatricula - gasto_anterior
                    diferenciaTransporte = estudiante.transporteBeca
                    diferenciaAlimentacion = estudiante.alimentacionBeca
                elif categoriaGasto == "transporte":
                    diferenciaMatricula = estudiante.matriculaBeca
                    diferenciaTransporte = dineroTransporte - gasto_anterior
                    diferenciaAlimentacion = estudiante.alimentacionBeca
                else:
                    diferenciaMatricula = estudiante.matriculaBeca
                    diferenciaTransporte = estudiante.transporteBeca
                    diferenciaAlimentacion = dineroAlimentacion - gasto_anterior

                if diferenciaMatricula < 0 or diferenciaAlimentacion < 0 or diferenciaTransporte < 0:
                    instancia.save()
                    messages.error(request, 'No hay fondos suficientes')
                else:
                    instancia.dineroAsignado = diferencia_gasto
                    instancia.alimentacionBeca = diferenciaAlimentacion
                    instancia.transporteBeca = diferenciaTransporte
                    instancia.matriculaBeca = diferenciaMatricula

                    descripcion = f"Gasto {request.POST['categoriaGasto']}: -{instancia.gasto} Fecha: {request.POST['fecha']}"
                    historialGasto = HistorialGastos(informacion_financiera=instancia, descripcion=descripcion)
                    historialGasto.save()

                    descripcionAlerta = f"Gasto {request.POST['categoriaGasto']}: -{instancia.gasto} Fecha: {request.POST['fecha']}"
                    titleAlerta = f"Nuevo gasto registrado para el estudiante con codigo: {code}"
                    typeAlerta = 4
                    alertaGenerada = Alerta(title=titleAlerta,type=typeAlerta,description=descripcionAlerta)
                    alertaGenerada.save()
                    


                    instancia.gasto = 0
                    instancia.save()
                    
                    messages.success(request, 'Gastos registrados correctamente!')
                    messages.success(request, 'Actualización enviada a filantropia!')
                    
                    return redirect('/contabilidad/buscarEstud.html')
            data["form"] = formulario
    else:
        messages.error(request, 'No se ha registrado la Información Financiera del estudiante')
        return redirect('/contabilidad/buscarEstud.html')
    
    return render(request, 'modificar.html', data)


def enviarMensaje(request):
    if request.method == 'POST':

        title = request.POST.get('title')
        typeAlert = request.POST.get('typeAlert')
        description = request.POST.get('description')

        Alerta.objects.create(title=title,
                              type=typeAlert,
                              description=description)
        
    return render(request, 'enviarMensaje.html')

