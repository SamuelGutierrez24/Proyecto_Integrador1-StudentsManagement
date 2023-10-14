from django.shortcuts import render, redirect
from Icesi_Students_Management.models import Student, Materia, BalanceAcademico, Status, Nota, SeguimientoBeca, Alerta

def registroNotasBA(request):
    return render(request, 'registroNotasBA.html')

def RegMateria(request):
    #Toma de datos basicos del estudiante (Variables otorgadas por la pagina buscarEstudiante)
    estudName = request.session['estudData']['nombre']
    estudLastName = request.session['estudData']['apellido']
    estudCode = request.session['estudData']['codigo']

    #Busqueda y declaracion del estudiante segun los datos otorgados
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
        else:
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
                    
                    #Validacion de datos otorgados para distingir entre Actualizacion y Creacion
                    if balanceVerf != None and notaVerf != None:
                        #En caso de existir algun Balance Academico y Nota
                        
                        #Declaracion de variables para la comparacion
                        materiaCode = balanceVerf.materiaID.materia_code
                        materiaNombre = balanceVerf.materiaID.nombre
                        materiaCreditos = str(balanceVerf.materiaID.creditos)
                        materiaEstatus = balanceVerf.statusID.type
                        materiNota = str(notaVerf.notaFinal)
                        
                        if materiaCode == cod_materia and materiaNombre == nombreMateria and balanceVerf.materiaID.creditos != creditosMateria and materiaEstatus != estatusMateria and notaVerf.notaFinal != nota:
                            #Existe un cambio en la informacion de una materia
                            print("Actualiza la materia")
                            #Actualizacion de los campos de Materia
                            Materia.objects.filter(materia_code = cod_materia, nombre = nombreMateria).update(creditos = creditosMateria)
                            
                            #Actualizacion del estatus de la materia                   
                            statusUpdate = BalanceAcademico.objects.filter(SeguimientoBecaID = segBeca).first()
                            statusUpdate.statusID.type = estatusMateria
                            print(statusUpdate.statusID.type)
                            print(statusUpdate.statusID)
                            BalanceAcademico.objects.filter(SeguimientoBecaID = segBeca).update(statusID = statusUpdate.statusID)
                            
                            #Actualizo las notas que tengan el mismo Balance Academico con la nueva nota dijitada
                            Nota.objects.filter(BalanceAcademicoID = balanceVerf).update(notaFinal = nota)
                            
                            #Creacion de la alerta    
                            alerta = Alerta.objects.create(title = "Actualizacion del Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia afectada: \n" + nombreMateria)
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
                            alerta = Alerta.objects.create(title = "Creacion de Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia añadida: \n" + nombreMateria)
                            
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
                        alerta = Alerta.objects.create(title = "Creacion de Balance Academico(s) de " + estudName + " - " + estudCode, type = 3, description = "Materia añadida: \n" + nombreMateria)
                        
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