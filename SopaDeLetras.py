import random
import linecache
import sys

#FUNCIONES
def elegirTamanio():
    print("¿Con que tablero desea iniciar la partida?")
    print()
        #Le pedimos al usuario que elija el tamanio del tablero
    print("ELIJA EL TAMAÑO DEL TABLERO")
    while True:
        try:
            print()
            tamanio=input("Ingrese C para jugar con el tablero chico, M para jugar con el tablero mediano o G para jugar con el tablero grande: ")
            tamanio=tamanio.upper()
            assert tamanio=="C" or tamanio=="M" or tamanio=="G"
            break
        except AssertionError:
            print("Solo puede ingresar C, M o G. Intente nuevamente.")
        #Asignamos la cantidad de celdas segun el tamanio elegido

    if tamanio=="C":
        n=10
    elif tamanio=="M":
        n=15
    else:
        n=20
    return n

def elegirDificultad(n):
    print()
    print("ELIJA LA DIFICULTAD DE LA PARTIDA")
    print("- Ingrese F para jugar con el tablero más fácil: las palabras pueden estar solo en direccion vertical de arriba hacia abajo u horizontal de izquierda a derecha)"+"\n\n"+ "- Ingrese M para jugar con el tablero de dificultad media: las palabras pueden estar en direccion vertical (en ambos sentidos), horizontal (en ambos sentidos) o en diagonal (solo de de izquierda a derecha y de arriba hacia abajo)"+"\n\n"+"- Ingrese D para jugar con el tablero más difícil: las palabras pueden estar en direcciion vertical (en ambos sentidos), horizontal (en ambos sentidos) o en diagonal (en ambas direcciones y cada una con sus dos sentidos)"+"\n\n"+"==> Ingrese el nivel de dificultad con el que quiere jugar: ")
    while True:
        try:
            print()
            dificultad=input("Ingrese F, M o D: ")
            dificultad=dificultad.upper()
            assert dificultad=="F" or dificultad=="M" or dificultad=="D"
            break
        except AssertionError:
            print("Solo puede ingresar F, M o D. Intente nuevamente.")
        #Asignamos la cantidad de palabras a buscar
    a = 0
    print()
    if dificultad=="F":
        a=2 #Cantidad de orientaciones que pueden tener las palabras
        mensaje="RECUERDE: Las palabras solo pueden estar en vetical u horizontal (en un unico sentido)"
        #Cantidad de palabras que tendra la sopa
        if n==10:
            d=4
        elif n==15:
            d=6
        elif n==20:
            d=8
    elif dificultad=="M":
        a=5
        mensaje="RECUERDE: Las palabras solo pueden estar en vetical (en ambos sentidos), horizontal (en ambos sentidos) o diagonal (solo de arriba hacia abajo e izquierda a derecha)"
        if n==10:
            d=5
        elif n==15:
            d=8
        else:
            d=10
    else:
        a=8
        mensaje="RECUERDE: Las palabras pueden estar en vetical, horizontal o diagonal, y en todos los sentidos"
        if n==10:
            d=6
        elif n==15:
            d=10
        else:
            d=12
    return d,a,mensaje

def elegirLista():
    print("ELIJA EL MODO DE JUEGO")
    while True:
        try:
            print()
            modo=input("Puede jugar buscando peliculas, animales, colores, paises o palabras random: ")
            modo=modo.lower()
            assert modo=="peliculas" or modo=="animales" or modo=="colores" or modo=="paises" or modo=="random"
            break
        except AssertionError:
            print("Ingrese uno de los modos de juego enumerados. Cuidado con la ortografia. Intente nuevamente: ")
    if modo=="random":
        return "palabras.txt"
    else:
        return modo+".txt"
    
def abrirArchivo(d, palabrasDelJuego, modoDeJuego):
            #Abrimos el archivo que contiene la lista de palabras
    try:
        archivo=open(modoDeJuego,"rt")
        if modoDeJuego=="palabras.txt":
            limite=250
        elif modoDeJuego=="animales.txt":
            limite=40
        elif modoDeJuego=="peliculas.txt":
            limite=24
        elif modoDeJuego=="paises.txt":
            limite=64
        else:
            limite=16
        lineasRandom=[] 
        for i in range(d+10):
            linea=random.randint(0,limite) 
            lineasRandom.append(linea) 
        lineasRandom.sort()
        inicio=0
        pos=0
        while len(palabrasDelJuego)<d:
            for i in range(inicio,lineasRandom[pos]): #Cuando se reinicia, empieza a leer a partir de la ultima palabra procesada
                archivo.readline() #Leemos las lineas pero no las guardamos
            palabra=archivo.readline()
            palabra=palabra.rstrip("\n")
            if len(palabra)<n: #Verificamos que entre en la matriz
                palabrasDelJuego.add(palabra)
            inicio=lineasRandom[pos]
            pos=pos+1
    except FileNotFoundError:
        print("Hubo un error al seleccionar las palabras de la sopa de letras")
    except OSError:
        print("Hubo un problema, intente mas tarde")
    finally:
        archivo.close()
    print()
    print("Las palabras a buscar son: "+ ', '.join(palabrasDelJuego)) #Mostramos las palabras a buscar
    print()
    return palabrasDelJuego
    
def rellenarMatriz(matriz,extension):
    n=len(matriz)
    palabrasParaUbicar=list(palabrasDelJuego) #Creamos una copia porque vamos a ir borrando palabras a medida que las ubiquemos
    while len(palabrasParaUbicar)>0: #Hasta insertar todas las palabras de la lista
        palabra=palabrasParaUbicar[0] #Seleccionamos la proxima palabra
        orientacion=random.randint(1,extension) #Elegimos la orientacion de manera aleatoria
        filaInicio=random.randint(0,n-1)  #Elegimos la celda en donde va a empezar la palabra
        columnaInicio=random.randint(0,n-1)
        ubicada=verificarEnVacio(orientacion,columnaInicio, palabra, filaInicio,palabrasParaUbicar)

    #Rellenamos los espacios que hayan quedado vacios
    
    for f in range (n):
        for c in range (n):
            posicion = random.randint (0,26)
            if matriz[f][c] == 0:
                matriz[f][c] = abecedario[posicion]
            
    #Funciones para verificar espacios
def haciaAbajo(filaInicio, palabra,columnaInicio):
    if n-filaInicio>=len(palabra): #Si entra en el espacio disponible,
        concat=""
        ceros=""
        for i in range(len(palabra)):
             ceros=ceros+"0"
        for i in range(len(palabra)):
            concat=concat+str(matriz[filaInicio+i][columnaInicio])
        if concat==ceros: #Y si no hay otra letra ubicada en esas celdas, agregamos la palabra
            for i in range(len(palabra)): 
                 matriz[filaInicio+i][columnaInicio]=palabra[i]
            return True

def haciaArriba(filaInicio, palabra,columnaInicio):
    if filaInicio>=len(palabra):    #Si entra,
        concat=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concat=concat+str(matriz[filaInicio-i][columnaInicio])
        if concat==ceros:   #y si no hay nada, la agregamos
            for i in range(len(palabra)):
                matriz[filaInicio-i][columnaInicio]=palabra[i]
            return True

def haciaLaDerecha(columnaInicio, palabra, filaInicio):
    if n-columnaInicio>=len(palabra):    #Si entra,
        concat=""
        ceros=""
        for i in range(len(palabra)):
             ceros=ceros+"0"
        for i in range(len(palabra)):
            concat=concat+str(matriz[filaInicio][columnaInicio+i])
        if concat==ceros:   #y si no hay nada, la agregamos
            for i in range(len(palabra)):
                matriz[filaInicio][columnaInicio+i]=palabra[i]
            return True
            
def haciaLaIzquierda(columnaInicio, palabra, filaInicio):
    if columnaInicio>=len(palabra):    #Si entra,
        concat=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concat=concat+str(matriz[filaInicio][columnaInicio-i])
        if concat==ceros:   #y si no hay nada, la agregamos
            for i in range(len(palabra)):
                matriz[filaInicio][columnaInicio-i]=palabra[i]
            return True
            
def haciaSupDerecha(columnaInicio, palabra, filaInicio):    
    if n-columnaInicio>=len(palabra) and filaInicio>=len(palabra):    #Si entra,
        concat=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concat=concat+str(matriz[filaInicio-i][columnaInicio+i])
        if concat==ceros:   #y si no hay nada, la agregamos
            for i in range(len(palabra)):
                matriz[filaInicio-i][columnaInicio+i]=palabra[i]
            return True
            
def haciaInfDerecha(columnaInicio, palabra, filaInicio):  
    if n-columnaInicio>=len(palabra) and n-filaInicio>=len(palabra):    #Si entra,
        concat=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concat=concat+str(matriz[filaInicio+i][columnaInicio+i])
        if concat==ceros:   #y si no hay nada, la agregamos
            for i in range(len(palabra)):
                matriz[filaInicio+i][columnaInicio+i]=palabra[i]
            return True
            
def haciaSupIzquierda(columnaInicio, palabra, filaInicio):
    if columnaInicio>=len(palabra) and filaInicio>=len(palabra):    #Si entra,
        concat=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concat=concat+str(matriz[filaInicio-i][columnaInicio-i])
        if concat==ceros:   #y si no hay nada, la agregamos
            for i in range(len(palabra)):
                matriz[filaInicio-i][columnaInicio-i]=palabra[i]
            return True
            
def haciaInfIzq(columnaInicio, palabra, filaInicio):       
    if n-columnaInicio>=len(palabra) and n-filaInicio>=len(palabra):    #Si entra,
        concat=""
        ceros=""
        for i in range(len(palabra)):
            ceros=ceros+"0"
        for i in range(len(palabra)):
            concat=concat+str(matriz[filaInicio+i][columnaInicio+i])
        if concat==ceros:   #y si no hay nada, la agregamos
            for i in range(len(palabra)):
                matriz[filaInicio+i][columnaInicio+i]=palabra[i]
            return True

def verificarEnVacio(orientacion,columnaInicio, palabra, filaInicio,palabrasParaUbicar):
    if orientacion==1: #Vertical normal
        ubicada=haciaAbajo(filaInicio, palabra, columnaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0) #La borramos de la lista, ya no hace falta ubicarla
    elif orientacion==2: #Horizontal normal
        ubicada=haciaLaDerecha(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==3: #Diagonal de izq a derecha y hacia abajo
        ubicada=haciaInfDerecha(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==4: #Vertical hacia arriba
        ubicada=haciaArriba(filaInicio, palabra, columnaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==5: #Horizontal invertida
        ubicada=haciaLaIzquierda(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==6: #Diagonal de izq a derecha y hacia arriba
        ubicada=haciaSupDerecha(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==7: #Diagonal de derecha a izq y hacia arriba
        ubicada=haciaSupIzquierda(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)
    elif orientacion==8: #Diagonal de derecha a izq y hacia abajo
        ubicada=haciaInfIzq(columnaInicio, palabra, filaInicio)
        if ubicada==True:
            palabrasParaUbicar.pop(0)

def imprimirMatriz(matriz):
    print ("    ","%2s"%"1",end="") #Enumeramos las columnas segun el tamanio de la matriz
    for i in range(len(matriz)-1):
        print("%4s"%str(i+2),end="")
    print()
    print ("    ","%2s"%"-", end="")
    for i in range(len(matriz)-1):
        print("%4s"%"-",end="")
    print()
    """x = 0
    for fila in matriz:                #Enumeramos las filas con letras
        print (abecedario[x], "|",end = "")
        x = x + 1
        for elem in fila:
            print("%4s" %elem, end="")
        print()"""
    x=0
    for i in range(len(matriz)):
        print (abecedario[x], "|",end = "")
        imprimirLista(matriz[i])
        print()
        x=x+1
        
def imprimirLista(lista, inicio=0):
    if inicio<len(lista):
        print("%4s" %lista[inicio],end="")
        imprimirLista(lista, inicio+1)
        
def imprimirConColor(matriz, filaInicio, columnaInicio, filaFin, columnaFin, palabra, coordenadas):
    filas=len(matriz)
    columnas=len(matriz[0])
    coordNuevas=concatenarCoordenadas (matriz,filaInicio,columnaInicio,filaFin,columnaFin)
    coordenadas=coordenadas+coordNuevas   
    try:
        color = sys.stdout.shell
    except AttributeError:
        raise RuntimeError("Use IDLE")

    print ("    ","%2s"%"1",end="") #Enumeramos las columnas segun el tamanio de la matriz
    for i in range(len(matriz)-1):
        print("%4s"%str(i+2),end="")
    print()
    print ("    ","%2s"%"-", end="")
    for i in range(len(matriz)-1):
        print("%4s"%"-",end="")
    print()  #Hasta aca es el encabezado
    x = 0
    for f in range (filas):                #Enumeramos las filas con letras
        print (abecedario[x], "|",end = "") 
        x = x + 1
        for c in range(columnas):
            if ((f,c)in coordenadas):
                color.write("%4s" %matriz[f][c], "STRING")
            else:
                print("%4s" %matriz[f][c], end="")
        print()
    return coordenadas

def validarCelda():
    while True:
        try:    #float para mostrar la razon exacta
            celda=input()
            letra=celda[0].upper()
            assert letra.isalpha(), "Error, el primer caracter de la celda debe ser la letra de la fila seleccionada. Intente nuevamente:"
            if n==10:
                assert letra in abecedario[:10], "Error, la fila ingresada esta fuera de rango. Intente nuevamente:"
                if len(celda)==2:
                    nro=int(celda[1])
                    assert nro<=10,"Error, la columna ingresada esta fuera de rango. Intente nuevamente:"
                else:
                    nro=int(celda[1]+celda[2])
                    assert nro<=10,"Error, la columna ingresada esta fuera de rango. Intente nuevamente:"
            elif n==15:
                assert letra in abecedario[:15], "Error, la fila ingresada esta fuera de rango. Intente nuevamente:"
                if len(celda)==2:
                    nro=int(celda[1])
                    assert nro<=15,"Error, la columna ingresada esta fuera de rango. Intente nuevamente:"
                else:
                    nro=int(celda[1]+celda[2])
                    assert nro<=15,"Error, la columna ingresada esta fuera de rango. Intente nuevamente:"
            elif n==20:
                assert letra in abecedario[:20], "Error, la fila ingresada esta fuera de rango. Intente nuevamente:"
                if len(celda)==2:
                    nro=int(celda[1])
                    assert nro<=20,"Error, la columna ingresada esta fuera de rango. Intente nuevamente:"
                else:
                    nro=int(celda[1]+celda[2])
                    assert nro<=20,"Error, la columna ingresada esta fuera de rango. Intente nuevamente:"
            assert str(nro).isdigit(), "Error, la segunda parte de la coordenada debe ser el numero de la columna seleccionada. Intente nuevamente:"
            break
        except AssertionError as mensaje:
            print(mensaje)
        except ValueError:
            print("Solo puede ingresar caracteres alfanumericos. Intente nuevamente: ")
    strAbecedario=''.join(abecedario)
    fila=strAbecedario.find(letra)
    return fila,nro #tupla

def concatenarLetras (mat,coorX1,coorY1,coorX2,coorY2): 
    palabra = mat[coorX1][coorY1] #palabra que se forma entre las coordenadas enviadas
    while coorX1 != coorX2 or coorY1 != coorY2:
        if coorX1 < coorX2:
            coorX1 += 1
        elif coorX1 > coorX2:
            coorX1 -= 1
            
        if coorY1 < coorY2:
            coorY1 += 1
        elif coorY1 > coorY2:
            coorY1 -= 1
        palabra = palabra + mat[coorX1][coorY1]
    return palabra

def concatenarCoordenadas (mat,coorX1,coorY1,coorX2,coorY2):
    coordenadas=[]
    coordenadas.append((coorX1,coorY1-1)) #palabra que se forma entre las coordenadas enviadas
    while coorX1 != coorX2 or coorY1 != coorY2:
        if coorX1 < coorX2:
            coorX1 += 1
        elif coorX1 > coorX2:
            coorX1 -= 1
            
        if coorY1 < coorY2:
            coorY1 += 1
        elif coorY1 > coorY2:
            coorY1 -= 1
        encontradas.append((coorX1,coorY1-1))
    return coordenadas

        
#PROGRAMA PRINCIPAL
print("BIENVENIDOS A NUESTRA SOPA DE LETRAS")
print()

terminar = ""

while terminar == "":
    n=elegirTamanio()
    d,a,mensaje=elegirDificultad(n)
    palabrasDelJuego=set() #Creamos un conjunto en donde vamos a agregar las palabras que seran usadas en el juego
    modoDeJuego=elegirLista()
    #---------
    palabrasDelJuego=abrirArchivo(d, palabrasDelJuego, modoDeJuego)

        #Creacion y relleno de matriz
    matriz=[[0]*(n) for i in range(n)]
    abecedario = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    rellenarMatriz(matriz,a)
    imprimirMatriz(matriz)
    #--------
    print()
    print(mensaje) #Recordatorio para el usuario
    
        #EMPIEZA EL JUEGO
    escape="" #Vamos a darle al usuario la posibilidad de salir del juego cuando quiera
    palabrasRestantes=list(palabrasDelJuego)
    while len(palabrasRestantes)>0 and escape=="":
        print()
        print("Ingrese la celda en la que empieza la palabra encontrada en formato 'A1': ")
        filaInicio, columnaInicio=validarCelda()
        print("Ingrese la celda en la que termina la palabra encontrada: ")
        filaFin, columnaFin=validarCelda()
        #Formamos la palabra que se encuentra entre las celdas elegidas
        palabraFormada=concatenarLetras(matriz,filaInicio,columnaInicio-1,filaFin,columnaFin-1)#Le restamos 1 porque el usuario empieza a contar en 1, no en 0
        if palabraFormada in palabrasDelJuego: #Si es una de las palabras que tenia que encontrar, ha cumplido el objetivo
            print("¡Felicitaciones! Ha encontrado la palabra", palabraFormada)
            if palabraFormada in palabrasRestantes:
                palabrasRestantes.remove(palabraFormada)
            if len(palabrasRestantes)>0:
                print("Las palabras que quedan son: "+', '.join(palabrasRestantes))
                encontradas=[]
                print()
                encontradas+=imprimirConColor(matriz, filaInicio, columnaInicio, filaFin, columnaFin, palabraFormada, encontradas)
                print()
                escape=input("Ingrese un 1 si desea salir del juego, o presione enter para continuar: ")
                print ()
        else:
            print("La palabra que ha seleccionado no se encuentra en la sopa. Siga intentando.")
            print ()
            escape=input("Ingrese un 1 si desea salir de la partida, o presione enter para continuar: ")

    if escape=="":
        print()
        print("¡FELICIDADES! Ha completado el juego.")
    else:
        print()
        print("El juego ha sido finalizado.")
    print ()
    terminar = input ("Ingrese 1 si quiere terminar, o presione enter para empezar una nueva partida: ")
    
    if terminar == "":
        print ("-"*125)
print("EL JUEGO HA FINALIZADO")
print("¡Esperamos que se haya divertido!")

