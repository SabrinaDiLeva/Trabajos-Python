"""11) Una clinica necesita un programa para atender a sus pacientes.
Cada paciente que ingresa se anuncia en la recepcion indicando
su numero de afiliado (nro entero de 4 digitos) y ademas indica
si viene por una urgenia (ingrsando un o) o con turno (1).
Para finalizar se ingresa -1 como numero de socio.
Luego se solicita:
a. Mostrar un listado de los pacientes atendidos por urgenia y
un listado de los pacientes atendidos por turno en el orden
en que llegaron a la clinica.
b. Realizar la busqueda de un numero de afiliado e informar
cuantas veces fue atendido por turno y cuantas por urgencia.
Repetir la busqueda hasta que se ingrese -1 como numero de afiliado """
#FUNCIONES
    #revisa que el nro de afiliado tenga 4 digitos
def validarPaciente(afiliado):
    while afiliado/1000<1 and afiliado!=-1:
        afiliado=int(input("Invalido. Ingrese el numero de afiliado. -1 para finalizar: "))
    while afiliado/10000>1:
        afiliado=int(input("Invalido. Ingrese el numero de afiliado. -1 para finalizar: "))
    return(afiliado)

    #input del nro de afiliado y tipo de atencion requerida
def agregarPaciente():
    afiliado=int(input("Ingrese su numero de afiliado. -1 para finalizar: "))
    afiliado=validarPaciente(afiliado) #si es invalido, quiero que se reescriba la variable
    if afiliado!=-1:
        atencion=int(input("Ingrese un 0 si necesita ser atendido de urgencia, o un 1 si tiene turno: "))
        while atencion!=0 and atencion!=1:
            atencion=int(input("Invalido. Ingrese un 0 si necesita ser atendido de urgencia, o un 1 si tiene turno: "))
    else:
        atencion=-1
        
    return(afiliado,atencion)

    #arma las listas segun el tipo de atencion recibida
def armarListas(atencion):
    if atencion==0:
        urgencia.append(afiliado)
    elif atencion==1:
        turno.append(afiliado)

    #cuenta la cantidad de veces que el paciente aparece en cada lista
def buscarPaciente(afiliado):
    cont_urg=urgencia.count(afiliado)
    cont_turno=turno.count(afiliado)
    return(cont_urg,cont_turno)

#PROGRAMA PRINCIPAL
urgencia=[]
turno=[]
    #se agregan usuarios hasta que se ingrese un -1
afiliado, atencion=agregarPaciente()
armarListas(atencion)
while afiliado!=-1:
    afiliado, atencion=agregarPaciente()
    armarListas(atencion)
    
    #muestro listas
print("Atendidos de urgencia: ", urgencia)
print("Atendidos con turno: ", turno)

    #paciente a buscar
afiliado=int(input("Ingrese su numero de afiliado a buscar. -1 para finalizar: "))
afiliado=validarPaciente(afiliado) #si es invalido, quiero que se reescriba la variable
while afiliado!=-1:
    cont_urg, cont_turno= buscarPaciente(afiliado)
        #muestro resultado de la busqueda
    print("El paciente", afiliado, "se atendio", cont_urg, "veces en urgencia y", cont_turno, "veces con turno")
        #ingreso numero de nuevo paciente a buscar
    afiliado=int(input("Ingrese su numero de afiliado a buscar. -1 para finalizar: "))
    afiliado=validarPaciente(afiliado)
print("Ha finalizado el proceso")
