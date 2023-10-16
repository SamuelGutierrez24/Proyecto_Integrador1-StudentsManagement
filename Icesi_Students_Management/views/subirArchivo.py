from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from ..models import HistorialGastos

def fileUpload(request):
    if request.method == 'POST' and request.FILES['comprobantePago']:
        comprobantePago = request.FILES['comprobantePago']
        fs = FileSystemStorage()
        comprobantePagoName = fs.save(comprobantePago.name, comprobantePago)

        # Obtén la instancia de HistorialGastos asociada
        historialGastoID = request.POST.get('historialGastoID')
        historialGastos = HistorialGastos.objects.get(pk=historialGastoID)

        # Asocia el archivo PDF con el historial de gastos
        historialGastos.comprobantePago = comprobantePagoName
        historialGastos.save()

        return render(request, 'modificar.html', {
            'archivo_pdf_url': fs.url(comprobantePagoName),
            'historialGastos': historialGastos
        })
    return render(request, 'modificar.html')
