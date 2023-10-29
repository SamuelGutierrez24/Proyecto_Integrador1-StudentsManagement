from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student, Materia, BalanceAcademico, Status, Nota, SeguimientoBeca, Alerta
import pandas as pd

def registroNotasBA(request):
    return render(request, 'registroNotasBA.html')

def RegMateria(request):
    #Toma de datos basicos del estudiante (Variables otorgadas por la pagina buscarEstudiante)
    estudName = request.session['estudData']['nombre']
    estudLastName = request.session['estudData']['apellido']
    estudCode = request.session['estudData']['codigo']

    #Busqueda y declaracion del estudiante segun los datos otorsgados
    student = Student.objects.get(code = estudCode)
    segimientobeca = SeguimientoBeca.objects.get(studentID = student)
    balance_academico = BalanceAcademico.objects.filter(SeguimientoBecaID=segimientobeca)
    
    #Obtencion de los datos ya existentes del estudiante   (Variable usada para la generacion automatica del formulario en el HTML)
    detalles = []
    for ba in balance_academico:
        materia = ba.materiaID
        status = ba.statusID
        nota = Nota.objects.get(BalanceAcademicoID=ba)
        detalles.append({
            'CodigoMateria': materia.materia_code,
            'NombreMateria': materia.nombre,
            'CreditosMateria': materia.creditos,
            'EstatusMateria': status.type,
            'NotaFinal': nota.notaFinal,
        })
    
    #Cantidad de balances academicos del estudiante     (Variable usada para la generacion automatica del formulario en el HTML)
    ultimo_contador = len(detalles) if detalles else 1
    
    if request.method == 'POST':
        studCode = request.session['estudData']['codigo']
        
        estudiante = Student.objects.all().filter(code=studCode).exists()
        print(estudiante)
        
        if estudiante == False:
            #No existe ningun estudiante con el codigo para registrarle materias
            return  render(request, 'registroNotasBA.html',{
                "error": 'El estudiante no existe', 
                'nombre': estudName, 
                'apellido':estudLastName, 
                'codigo':estudCode, 
                'detalles': detalles, 
                'ultimoContador': ultimo_contador
                })
        
        elif 'file' in request.FILES and not request.POST.get('codMateria1'):
            archivo_excel = request.FILES['file']
            print("Entra a archivo - no hay form")
            if archivo_excel.name.endswith('.xlsx'):
                df = pd.read_excel(archivo_excel, engine='openpyxl')

                for index, row in df.iterrows():
                    cod_materiaXLS = row['codMateria']
                    nombreMateriaXLS = row['nombreMateria']
                    creditosMateriaXLS = row['creditosMateria']
                    estatusMateriaXLS = row['estatusMateria']
                    notaXLS = row['Nota']
                    
                    segBeca = SeguimientoBeca.objects.get(studentID = student)
                    
                    try:
                        balanceVerf = BalanceAcademico.objects.get(SeguimientoBecaID = segBeca, materiaID = Materia.objects.get(materia_code = cod_materiaXLS))
                        notaVerf = Nota.objects.get(BalanceAcademicoID = balanceVerf)
                    except:
                        balanceVerf = None
                        notaVerf = None

                    if balanceVerf != None and notaVerf != None:
                        #En caso de existir algun Balance Academico y Nota
                                    
                        #Declaracion de variables para la comparacion
                        materiaCode = balanceVerf.materiaID.materia_code
                        materiaNombre = balanceVerf.materiaID.nombre
                        materiaCreditos = str(balanceVerf.materiaID.creditos)
                        materiaEstatus = balanceVerf.statusID.type
                        materiNota = str(notaVerf.notaFinal)
                                    
                        if materiaCode == cod_materiaXLS and materiaNombre == nombreMateriaXLS and materiaCreditos == creditosMateriaXLS and materiaEstatus != estatusMateriaXLS or materiNota != notaXLS:
                            #Existe un cambio en la informacion de una materia
                            print("Actualiza la materia")
                            #Actualizacion de los campos de Materia
                            Materia.objects.filter(materia_code = cod_materiaXLS, nombre = nombreMateriaXLS).update(creditos = creditosMateriaXLS)
                                        
                            #Actualizacion del estatus de la materia
                            balanceUpdate = BalanceAcademico.objects.filter(SeguimientoBecaID = segBeca, materiaID = Materia.objects.get(materia_code = cod_materiaXLS)).first()
                            Status.objects.filter(StatusID = balanceUpdate.statusID.StatusID).update(type = estatusMateriaXLS)
                                        
                            #Actualizo las notas que tengan el mismo Balance Academico con la nueva nota dijitada
                            Nota.objects.filter(BalanceAcademicoID = balanceVerf).update(notaFinal = notaXLS)
                                        
                            #Creacion de la alerta    
                            alerta = Alerta.objects.create(title = "Actualizacion del Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia afectada: \n" + nombreMateriaXLS, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                            alerta.save()
                                            
                            continue
                        elif materiaCode == cod_materiaXLS and materiaNombre == nombreMateriaXLS and materiaCreditos == creditosMateriaXLS and materiaEstatus == estatusMateriaXLS and materiNota == notaXLS:                          
                            #Existe una materia pero esta no tiene ningun cambio con respecto a la base de datos. No se registran actualizaciones ni registros nuevos
                            print("Se salta la materia")
                            continue   
                        else:
                            #No existe una materia en la base de datos con la informacion proporcionada. Se registra la nueva materia y su balance
                            print("Crea una materia")
                            #Creacion de la alerta
                            alerta = Alerta.objects.create(title = "Creacion de Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia añadida: \n" + nombreMateriaXLS, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                                        
                            #Creacion de la materia, balance academico y demas
                            statusMateria = Status.objects.create(type=estatusMateriaXLS)
                            materia = Materia.objects.create(materia_code = cod_materiaXLS, nombre= nombreMateriaXLS, creditos= creditosMateriaXLS)
                            balanceAcademico = BalanceAcademico.objects.create(statusID = statusMateria, materiaID = materia, SeguimientoBecaID = segBeca)   
                            notaFinal = Nota.objects.create(BalanceAcademicoID = balanceAcademico, notaFinal = notaXLS)
                            alerta.save()
                            materia.save()
                            statusMateria.save()
                            balanceAcademico.save()
                            notaFinal.save()
                            continue
                    else:
                        #En caso de no existir ningun Balance Academico
                        #Crea la materia y el Balance academico para el estudainte
                        print("Crea una materia inexistente")
                        #Creacion de la alerta para el menu de Balance Academico
                        alerta = Alerta.objects.create(title = "Creacion de Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia añadida: \n" + nombreMateriaXLS, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                                    
                        statusMateria = Status.objects.create(type=estatusMateriaXLS)
                        materia = Materia.objects.create(materia_code = cod_materiaXLS, nombre= nombreMateriaXLS, creditos= creditosMateriaXLS)
                        balanceAcademico = BalanceAcademico.objects.create(statusID = statusMateria, materiaID = materia, SeguimientoBecaID = segBeca)   
                        notaFinal = Nota.objects.create(BalanceAcademicoID = balanceAcademico, notaFinal = notaXLS)
                        alerta.save()
                        materia.save()
                        statusMateria.save()
                        balanceAcademico.save()
                        notaFinal.save()
                        continue
                                
                return redirect('menuBalanceAcademico')  
        
        else:
            print("Entra a archivo - hay form")
            for key, value in request.POST.items():
                if key.startswith('codMateria') and value:
                    #Toma de datos del formulario    
                    index = key.replace('codMateria', '')
                    cod_materia = request.POST[f'codMateria{index}']
                    nombreMateria = request.POST[f'nombreMateria{index}']
                    creditosMateria = request.POST[f'creditosMateria{index}']
                    estatusMateria = request.POST[f'estatusMateria{index}']
                    nota = request.POST[f'Nota{index}']
                    
                    segBeca = SeguimientoBeca.objects.get(studentID = student)
                    
                    try:
                        balanceVerf = BalanceAcademico.objects.get(SeguimientoBecaID = segBeca, materiaID = Materia.objects.get(materia_code = cod_materia))
                        notaVerf = Nota.objects.get(BalanceAcademicoID = balanceVerf)
                    except:
                        balanceVerf = None
                        notaVerf = None
                    
                    if 'file' in request.FILES:
                        archivo_excel = request.FILES['files']
                        print("Entra a archivo - si hay cosas en el form")
                        if archivo_excel.name.endswith('.xlsx'):
                            df = pd.read_excel(archivo_excel, engine='openpyxl')

                            for index, row in df.iterrows():
                                cod_materiaXLS = row['codMateria']
                                nombreMateriaXLS = row['nombreMateria']
                                creditosMateriaXLS = row['creditosMateria']
                                estatusMateriaXLS = row['estatusMateria']
                                notaXLS = row['Nota']

                                if balanceVerf != None and notaVerf != None:
                                    #En caso de existir algun Balance Academico y Nota
                                    
                                    #Declaracion de variables para la comparacion
                                    materiaCode = balanceVerf.materiaID.materia_code
                                    materiaNombre = balanceVerf.materiaID.nombre
                                    materiaCreditos = str(balanceVerf.materiaID.creditos)
                                    materiaEstatus = balanceVerf.statusID.type
                                    materiNota = str(notaVerf.notaFinal)
                                    
                                    if materiaCode == cod_materia and materiaCode == cod_materiaXLS and materiaNombre == nombreMateria and materiaNombre == nombreMateriaXLS and materiaCreditos == creditosMateria and materiaCreditos == creditosMateriaXLS and materiaEstatus != estatusMateria and materiaEstatus != estatusMateriaXLS or materiNota != nota and materiNota != notaXLS:
                                        #Existe un cambio en la informacion de una materia
                                        print("Actualiza la materia")
                                        #Actualizacion de los campos de Materia
                                        Materia.objects.filter(materia_code = cod_materiaXLS, nombre = nombreMateriaXLS).update(creditos = creditosMateriaXLS)
                                        
                                        #Actualizacion del estatus de la materia   
                                        balanceUpdate = BalanceAcademico.objects.filter(SeguimientoBecaID = segBeca, materiaID = Materia.objects.get(materia_code = cod_materiaXLS)).first()
                                        Status.objects.filter(StatusID = balanceUpdate.statusID.StatusID).update(type = estatusMateriaXLS)
                                        
                                        #Actualizo las notas que tengan el mismo Balance Academico con la nueva nota dijitada
                                        Nota.objects.filter(BalanceAcademicoID = balanceVerf).update(notaFinal = notaXLS)
                                        
                                        #Creacion de la alerta    
                                        alerta = Alerta.objects.create(title = "Actualizacion del Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia afectada: \n" + nombreMateriaXLS, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                                        alerta.save()
                                            
                                        continue
                                    elif materiaCode == cod_materia and materiaCode == cod_materiaXLS and materiaNombre == nombreMateria and materiaNombre == nombreMateriaXLS and materiaCreditos == creditosMateria and materiaCreditos == creditosMateriaXLS and materiaEstatus == estatusMateria and materiaEstatus == estatusMateriaXLS and materiNota == nota and materiNota == notaXLS:                          
                                        #Existe una materia pero esta no tiene ningun cambio con respecto a la base de datos. No se registran actualizaciones ni registros nuevos
                                        print("Se salta la materia")
                                        continue   
                                    else:
                                        #No existe una materia en la base de datos con la informacion proporcionada. Se registra la nueva materia y su balance
                                        print("Crea una materia")
                                        #Creacion de la alerta
                                        alerta = Alerta.objects.create(title = "Creacion de Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia añadida: \n" + nombreMateriaXLS, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                                        
                                        #Creacion de la materia, balance academico y demas
                                        statusMateria = Status.objects.create(type=estatusMateriaXLS)
                                        materia = Materia.objects.create(materia_code = cod_materiaXLS, nombre= nombreMateriaXLS, creditos= creditosMateriaXLS)
                                        balanceAcademico = BalanceAcademico.objects.create(statusID = statusMateria, materiaID = materia, SeguimientoBecaID = segBeca)   
                                        notaFinal = Nota.objects.create(BalanceAcademicoID = balanceAcademico, notaFinal = notaXLS)
                                        alerta.save()
                                        materia.save()
                                        statusMateria.save()
                                        balanceAcademico.save()
                                        notaFinal.save()
                                        continue
                                else:
                                    #En caso de no existir ningun Balance Academico
                                    #Crea la materia y el Balance academico para el estudainte
                                    print("Crea una materia inexistente")
                                    #Creacion de la alerta para el menu de Balance Academico
                                    alerta = Alerta.objects.create(title = "Creacion de Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia añadida: \n" + nombreMateriaXLS, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                                    
                                    statusMateria = Status.objects.create(type=estatusMateriaXLS)
                                    materia = Materia.objects.create(materia_code = cod_materiaXLS, nombre= nombreMateriaXLS, creditos= creditosMateriaXLS)
                                    balanceAcademico = BalanceAcademico.objects.create(statusID = statusMateria, materiaID = materia, SeguimientoBecaID = segBeca)   
                                    notaFinal = Nota.objects.create(BalanceAcademicoID = balanceAcademico, notaFinal = notaXLS)
                                    alerta.save()
                                    materia.save()
                                    statusMateria.save()
                                    balanceAcademico.save()
                                    notaFinal.save()
                                    continue
                                
                            return redirect('menuBalanceAcademico')  
                    
                    #Validacion de datos otorgados para distingir entre Actualizacion y Creacion
                    elif balanceVerf != None and notaVerf != None:
                        #En caso de existir algun Balance Academico y Nota
                        print("entra elif")
                        #Declaracion de variables para la comparacion
                        materiaCode = balanceVerf.materiaID.materia_code
                        materiaNombre = balanceVerf.materiaID.nombre
                        materiaCreditos = str(balanceVerf.materiaID.creditos)
                        materiaEstatus = balanceVerf.statusID.type
                        materiNota = str(notaVerf.notaFinal)
                        
                        if materiaCode == cod_materia and materiaNombre == nombreMateria and materiaCreditos == creditosMateria and materiaEstatus != estatusMateria or materiNota != nota:
                            #Existe un cambio en la informacion de una materia
                            print("Actualiza la materia")
                            #Actualizacion de los campos de Materia
                            Materia.objects.filter(materia_code = cod_materia, nombre = nombreMateria).update(creditos = creditosMateria)
                            
                            #Actualizacion del estatus de la materia                   
                            balanceUpdate = BalanceAcademico.objects.filter(SeguimientoBecaID = segBeca, materiaID = Materia.objects.get(materia_code = cod_materia)).first()
                            Status.objects.filter(StatusID = balanceUpdate.statusID.StatusID).update(type = estatusMateria)
                            
                            #Actualizo las notas que tengan el mismo Balance Academico con la nueva nota dijitada
                            Nota.objects.filter(BalanceAcademicoID = balanceVerf).update(notaFinal = nota)
                            
                            #Creacion de la alerta    
                            alerta = Alerta.objects.create(title = "Actualizacion del Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia afectada: \n" + nombreMateria, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                            alerta.save()
                                
                            continue
                        elif materiaCode == cod_materia and materiaNombre == nombreMateria and materiaCreditos == creditosMateria and materiaEstatus == estatusMateria and materiNota == nota:                          
                            #Existe una materia pero esta no tiene ningun cambio con respecto a la base de datos. No se registran actualizaciones ni registros nuevos
                            print("Se salta la materia")
                            continue   
                        else:
                            #No existe una materia en la base de datos con la informacion proporcionada. Se registra la nueva materia y su balance
                            print("Crea una materia")
                            #Creacion de la alerta
                            alerta = Alerta.objects.create(title = "Creacion de Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia añadida: \n" + nombreMateria, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                            
                            #Creacion de la materia, balance academico y demas
                            statusMateria = Status.objects.create(type=estatusMateria)
                            materia = Materia.objects.create(materia_code = cod_materia, nombre= nombreMateria, creditos= creditosMateria)
                            balanceAcademico = BalanceAcademico.objects.create(statusID = statusMateria, materiaID = materia, SeguimientoBecaID = segBeca)   
                            notaFinal = Nota.objects.create(BalanceAcademicoID = balanceAcademico, notaFinal = nota)
                            alerta.save()
                            materia.save()
                            statusMateria.save()
                            balanceAcademico.save()
                            notaFinal.save()
                            continue
                    else:
                        #En caso de no existir ningun Balance Academico
                        #Crea la materia y el Balance academico para el estudainte
                        print("Crea una materia inexistente")
                        #Creacion de la alerta para el menu de Balance Academico
                        alerta = Alerta.objects.create(title = "Creacion de Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia añadida: \n" + nombreMateria, StudentID = SeguimientoBeca.objects.all().get(code = estudCode))
                        
                        statusMateria = Status.objects.create(type=estatusMateria)
                        materia = Materia.objects.create(materia_code = cod_materia, nombre= nombreMateria, creditos= creditosMateria)
                        balanceAcademico = BalanceAcademico.objects.create(statusID = statusMateria, materiaID = materia, SeguimientoBecaID = segBeca)   
                        notaFinal = Nota.objects.create(BalanceAcademicoID = balanceAcademico, notaFinal = nota)
                        alerta.save()
                        materia.save()
                        statusMateria.save()
                        balanceAcademico.save()
                        notaFinal.save()
                        continue
            return redirect('menuBalanceAcademico')              

    return render(request, 'registroNotasBA.html', {
        'nombre': estudName, 
        'apellido':estudLastName, 
        'codigo':estudCode, 
        'detalles': detalles, 
        'ultimoContador': ultimo_contador})