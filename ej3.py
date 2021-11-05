"""3)
Una institucion deportiva necesita clasificar a sus atletas para inscribirlos
en los proximos juegos panamericanos. Para eso se encargo la realizacion de
un programa que incluya las siguientes funciones:
a) grabarRangoAlturas() graba en un archivo las altura de los atletas de
distintas desciplinas, los que se ingresan desde el teclado. Cada dato
se debe grabar en una linea distinta. Ejemplo:
<deporte 1>
<altura del atleta 1>
<altura del atleta 2>
<...>
<deporte 2>
<altura del atleta 1>
<altura del atleta 2>
<...>

b) grabar promedio() graba en un archivo los promedios de las alturas de
los atletas presentes en el archivo generado en el paso anterior.
La disciplina y el promedio deben grabarse en lineas diferentes. Ejemplo:
<Deporte 1> 
<promedio alturas deporte 1>
<deporte 2>
<promedio alturas deporte 2>
<...>

c) mostrarMasAltos() muestra por pantalla las disciplinas deportivas cuyos
atletas superan la estatura promedio general. Obtener los datos del segundo archivo. """

print("Inicio de programa")
#FUNCIONES
def leerDeportista(): #ingreso deporte y altura del atleta, con ctrol de errores
    while True:
        try:
            deporte=input("Ingrese la disciplina del atleta, enter para terminar: ")
            if deporte!="":
                assert deporte.isalpha()
                altura= float(input("Ingrese la altura del atleta: "))
            else:
                altura=""
            break
        except AssertionError:
            print("Solo puede ingresar letras")
        except ValueError:
            print("El dato ingresado es invalido, intente nuevamente")
    return deporte, altura

#PROGRAMA PRINCIPAL
arrayDeportes=[]
arrayAlturas=[]

deporte,altura=leerDeportista()
print(deporte,altura)
arrayDeportes.append(deporte)
arrayAlturas.append(altura)
#arrayDeportes[0]=[]
#arrayDeportes[0].append(altura)

while deporte!="":
    deporte,altura=leerDeportista()
    arrayDeportes.append(deporte)
    arrayAlturas.append(altura)
if len(arrayAlturas)>1: #porque el ultimo dato va a ser vacio
    arrayDeportes.pop()
    arrayAlturas.pop()
print("Todos los deportes ingresados: ", arrayDeportes)
print("Todos las alturas ingresadas: ", arrayAlturas)
#print(arrayDeportes[0])
print("Fin de programa")












