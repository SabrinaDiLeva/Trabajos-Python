"""2)f)Escribir una funcion que genere la matriz
Tamanio N x N. Las funciones deben servir aunque los valores se modifiquen
0  0  0  1
0  0  3  2
0  6  5  4
10 9  8  7 """


def rellenar_matriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    #c=columnas-1
    a=1
    for f in range(filas):
        for c in range(1,f+2):
            matriz[f][-c]=a
            a=a+1
    
        
def imprimir_matriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

#Programa principal
n=int(input("Ingrese la cantidad de filas y columnas: "))
filas=n
columnas=n    #arma matriz solo con ceros
matriz=[[0]*columnas for i in range(filas)]

rellenar_matriz(matriz)
imprimir_matriz(matriz)


