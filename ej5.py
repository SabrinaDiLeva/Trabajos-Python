"""5)Programa para realizar reservas en una sala de cine de barrrio
de N filas con M butacas por cada fila.

a. mostrar_butacas: mostrara por pantalla el estado de cada una
de las butacas del cine por pantalla. Se debera mostrar antes
de que el usuario realice la reserva y se volvera a mostrar
luego de la misma, con los datos actualizados.

b. reservar: debera recibir una matriz y la butaca seleccionada,
y actualizara la matriz en caso de estar disponible dicha butaca
La funcion devolvera true/false si logro o no reservar la butaca

c. cargar_sala: recibira una matriz como parametro y la cargara
con valores aleatorios para simular la sala con butacas ya reservadas

d. butacas_libres: recibira como parametro la matriz y retornara
cuantas butacas desocupadas hay en la sala

e. butacas_contiguas: buscara la secuencia mas larga de butacas libres
contiguas en una misma fila y devolvera las coordenadas del inicio de la misma"""

import random
#Funciones
def cargar_sala(matriz): 
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            n=random.randint(0,1) #genero aleatoream el estado de la butaca
            matriz[f][c]=n
            
def mostrar_butacas(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()
        
def elegirButaca():
    fila_reserva=int(input("Ingrese la fila en la que quiere hacer la reserva: "))
    while fila_reserva<1 or fila_reserva>filas:
        fila_reserva=int(input("Invalido. Ingrese la fila en la que quiere hacer la reserva: "))
    col_reserva=int(input("Ingrese la butaca en la que quiere hacer la reserva: "))
    while col_reserva<1 or col_reserva>butacas:
        col_reserva=int(input("Invalido. Ingrese la butaca en la que quiere hacer la reserva: "))
    return fila_reserva, col_reserva


def reservar(f, b):
    if matriz[f][b]==0:
        matriz[f][b]=1
        return true
    else:
        return false

def concretar_reserva(reserva):
    if reserva==True:
        print("La reserva se ha realizado con exito")
        return 1
    else:
        print("La butaca ya esta ocupada")
        return -1

#Programa principal
        #se arma la matriz y se carga con valores aleatorios
filas=int(input("Ingrese la cantidad de filas: "))
butacas=int(input("Ingrese la cantidad de butacas por fila: "))
matriz=[[0]*butacas for i in range(filas)]
cargar_sala(matriz)

        #se muestra el estado de la sala
print()
print("Estado de la sala. 0=libres, 1=reservadas")
mostrar_butacas(matriz)

        #ingresa butaca a reservar
fila_reserva,col_reserva=elegirButaca()

        #se puede reservar esa butaca?
reserva=reservar(fila_reserva,col_reserva)
estado_reserva=concretar_reserva(reserva)
        #si no se pudo reservar, elegir otra
while resultado==-1:
    fila_reserva,col_reserva=elegirButaca()
    reserva=reservar(fila_reserva,col_reserva)
    estado_reserva=concretar_reserva(reserva)
        
