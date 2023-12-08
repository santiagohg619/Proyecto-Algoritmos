import random
# from fractions import Fraction
from math import gcd
from tabulate import tabulate

# Recordar comparar con valores string no enteros
# Descomentar si se desea fracciones simplificadas
# estadoCanal,sumEstado=simpFraccion(estadoCanal,sumEstado) en la funcion calcular_matriz_EstadoCanalF

muestrasBase = []
#Genera las 2^n posibilidades de n canales
def generar_muestras(numCanales):
    for i in range(2 ** numCanales):
        num = format(i, f'0{numCanales}b')
        muestrasBase.append(num)

def generar_estados_aleatorios(num_canales, num_muestras):
    estados_posibles = ["0", "1"]  # Estados posibles
    #Genera las entradas en el diccionario, con las letras del alfabeto secuancialmente y en mayusculas
    estados_generados = {f"{chr(65 + i)}": [] for i in range(num_canales)}
    # print("Estados generados en aleatorios para diccionario",estados_generados)

    for _ in range(num_muestras):
        for canal in estados_generados:
            estado_actual = random.choice(estados_posibles)
            estados_generados[canal].append(estado_actual)

    return estados_generados

def mostrar_estados(estados):
    for canal, estados_canal in estados.items():
        print(f"{canal}:", estados_canal)

# Junta los datos de los n canales en un solo string
def getEstado(canalesData, iteracion):
    res = ""
    for keys in canalesData:
        res += str(canalesData[keys][iteracion])
    return res

def simpFraccion(dividendo, divisor):
    #Halla el maximo comun divisor
    mcd=gcd(dividendo,divisor)

    if mcd!=1:
        dividendo=dividendo//mcd
        divisor=divisor//mcd
    
    return dividendo, divisor

def graphMatriz(matriz, opc):
    if opc=="+":
        titulosColumnas=["Estado//T+1"]
    elif opc=="-":
        titulosColumnas=["Estado//T-1"]
    otrosTitulos=matriz[list(matriz.keys())[0]].keys()
    titulosColumnas.extend(otrosTitulos)

    table = [[key] + [matriz[key][column] for column in titulosColumnas[1:]] for key in matriz.keys()]

    print(tabulate(table, titulosColumnas, tablefmt="fancy_grid"))


#Punto 1
# Función para calcular la matriz de probabilidades para los 1 en los canales y guardar los indexs
def calcular_matriz_EstadoCanalF(estados_canales,numMuestras):
    #Almacena los indices de los estados, para reutilizarlos en el calculo de las otras matrices de estados
    indexEstados= {muestra: [] for muestra in muestrasBase}
    EstadoCanalF = {estados: {canal: 0 for canal in estados_canales.keys()} for estados in muestrasBase}
    print("Matriz Inicial",EstadoCanalF)
    
    # Itera por cada una de las muestras
    for time in range(numMuestras):
        # Añade el index, en el que un estado posible aparece en la muestra
        temp = getEstado(estados_canales,time)
        indexEstados[temp].append(time)
        # print("Estoy en la iteracion",time+1)
        # Itera entre los canales en caso de no tratarse de la ultima muestra
        # Se usa el -1 para que se ajuste a la forma en la que se manejan los indexs (desde el cero hasta numMuestras-1)
        if(time!=(numMuestras-1)):
            # print("Ha entrado")
            for canal in estados_canales.keys():
                # print("Evaluando si hay un",canal ,"en UNO justo despues, para la muestra",muestra)
                # print("EL valor del canal ",canal,"en t+1 es:",estados_canales[canal][time+1])
                proxEstadoCanal= estados_canales[canal][time+1]
                EstadoCanalF[temp][canal] += int(proxEstadoCanal)

    # print("Matriz valores despues de iterar",EstadoCanalF)
    # print("Lista de ocurrencias",indexEstados)

    # Calcular las probabilidades dividiendo por el número de coincidencias del estado actual
    for estado in EstadoCanalF:
        for canal in EstadoCanalF[estado]:
            estadoCanal=EstadoCanalF[estado][canal]
            sumEstado= len(indexEstados[estado])
            #Por si el divisor es 0
            if(sumEstado==0):
                EstadoCanalF[estado][canal]="Indefinido"
            # Por si el dividendo es 0
            elif (estadoCanal==0):
                EstadoCanalF[estado][canal]=str(0)
            # Por si la dicision es exacta
            elif(estadoCanal%sumEstado==0):
                EstadoCanalF[estado][canal]=str(int(estadoCanal/sumEstado))
            # Por si la division no es exacta
            else:
                # Descomentar si se desea fracciones simplificadas
                # estadoCanal,sumEstado=simpFraccion(estadoCanal,sumEstado) 

                EstadoCanalF[estado][canal] =""+str(estadoCanal)+"/"+str(sumEstado)
            # EstadoCanalF[estado][canal] =Fraction(int(EstadoCanalF[estado][canal])/len(indexEstados[estado]))
    
    print("Matriz valores despues de operar",EstadoCanalF)

    return EstadoCanalF, indexEstados

#Punto 2
def generar_matriz_EstadoEstadoF(indexEstados):
    # Inicializar la matriz de probabilidades previas con ceros
    EstadoEstadoF = {estado: {estado: 0 for estado in muestrasBase} for estado in muestrasBase}
    print("Matriz inicial", EstadoEstadoF)
    
    #Iteracion n*n de estados 
    for estado in muestrasBase:
        for estadoNext in muestrasBase:
            for index in indexEstados[estado]:
                # print("actual",index)
                for indexNext in indexEstados[estadoNext]:
                    # print("next",indexNext)
                    if index+1 ==indexNext:
                        EstadoEstadoF[estado][estadoNext]+=1

    print("Matriz despues de iterar", EstadoEstadoF)

    # Calcular las probabilidades dividiendo por el número de coincidencias del estado actual
    for estado in EstadoEstadoF:
        for estadoNext in EstadoEstadoF[estado]:
            # print("valores",estado,"y",estadoNext,"son",EstadoEstadoF[estado][estadoNext])
            estadoMuestra=EstadoEstadoF[estado][estadoNext]
            # print("estadoMuestra",estadoMuestra)
            sumEstado= len(indexEstados[estado])
            # print("sumEstado",sumEstado)
            #Por si el divisor es 0
            if(sumEstado==0):
                EstadoEstadoF[estado][estadoNext]="Indefinido"
            # Por si el dividendo es 0
            elif (estadoMuestra==0):
                EstadoEstadoF[estado][estadoNext]=str(0)
            # Por si la dicision es exacta
            elif(estadoMuestra%sumEstado==0):
                EstadoEstadoF[estado][estadoNext]=str(int(estadoMuestra/sumEstado))
            # Por si la division no es exacta
            else:
                # Descomentar si se desea fracciones simplificadas
                # estadoMuestra,sumEstado=simpFraccion(estadoMuestra,sumEstado) 
                EstadoEstadoF[estado][estadoNext] =""+str(estadoMuestra)+"/"+str(sumEstado)
            # EstadoCanalF[estado][canal] =Fraction(int(EstadoCanalF[estado][canal])/len(indexEstados[estado]))
    
    print("Matriz valores despues de operar",EstadoEstadoF)

    return EstadoEstadoF

#Punto 3
def calcular_matriz_EstadoCanalP(estados_canales,numMuestras,indexEstados):
    EstadoCanalP = {estados: {canal: 0 for canal in estados_canales.keys()} for estados in muestrasBase}
    print("Matriz Inicial",EstadoCanalP)
    
    # Itera por cada una de las muestras
    for time in range(1,numMuestras):
        temp = getEstado(estados_canales,time)
        # print("Ha entrado")
        for canal in estados_canales.keys():
            prevEstadoCanal= estados_canales[canal][time-1]
            EstadoCanalP[temp][canal] += int(prevEstadoCanal)

    # print("Matriz valores despues de iterar",EstadoCanalF)
    # print("Lista de ocurrencias",indexEstados)

    # Calcular las probabilidades dividiendo por el número de coincidencias del estado actual
    for estado in EstadoCanalP:
        for canal in EstadoCanalP[estado]:
            estadoCanal=EstadoCanalP[estado][canal]
            sumEstado= len(indexEstados[estado])
            #Por si el divisor es 0
            if(sumEstado==0):
                EstadoCanalP[estado][canal]="Indefinido"
            # Por si el dividendo es 0
            elif (estadoCanal==0):
                EstadoCanalP[estado][canal]=str(0)
            # Por si la dicision es exacta
            elif(estadoCanal%sumEstado==0):
                EstadoCanalP[estado][canal]=str(int(estadoCanal/sumEstado))
            # Por si la division no es exacta
            else:
                # Descomentar si se desea fracciones simplificadas
                # estadoCanal,sumEstado=simpFraccion(estadoCanal,sumEstado) 

                EstadoCanalP[estado][canal] =""+str(estadoCanal)+"/"+str(sumEstado)
            # EstadoCanalF[estado][canal] =Fraction(int(EstadoCanalF[estado][canal])/len(indexEstados[estado]))
    
    print("Matriz valores despues de operar",EstadoCanalP)

    return EstadoCanalP

#Punto 4
def generar_matriz_EstadoEstadoP(indexEstados):
    # Inicializar la matriz de probabilidades previas con ceros
    EstadoEstadoP = {estado: {estado: 0 for estado in muestrasBase} for estado in muestrasBase}
    print("Matriz inicial", EstadoEstadoP)
    
    #Iteracion n*n de estados 
    for estado in muestrasBase:
        for estadoPrev in muestrasBase:
            for index in indexEstados[estado]:
                # print("actual",index)
                for indexPrev in indexEstados[estadoPrev]:
                    # print("next",indexNext)
                    if index-1 ==indexPrev:
                        EstadoEstadoP[estado][estadoPrev]+=1

    print("Matriz despues de iterar", EstadoEstadoP)

    # Calcular las probabilidades dividiendo por el número de coincidencias del estado actual
    for estado in EstadoEstadoP:
        for estadoPrev in EstadoEstadoP[estado]:
            # print("valores",estado,"y",estadoNext,"son",EstadoEstadoF[estado][estadoNext])
            estadoMuestra=EstadoEstadoP[estado][estadoPrev]
            # print("estadoMuestra",estadoMuestra)
            sumEstado= len(indexEstados[estado])
            # print("sumEstado",sumEstado)
            #Por si el divisor es 0
            if(sumEstado==0):
                EstadoEstadoP[estado][estadoPrev]="Indefinido"
            # Por si el dividendo es 0
            elif (estadoMuestra==0):
                EstadoEstadoP[estado][estadoPrev]=str(0)
            # Por si la dicision es exacta
            elif(estadoMuestra%sumEstado==0):
                EstadoEstadoP[estado][estadoPrev]=str(int(estadoMuestra/sumEstado))
            # Por si la division no es exacta
            else:
                # Descomentar si se desea fracciones simplificadas
                # estadoMuestra,sumEstado=simpFraccion(estadoMuestra,sumEstado) 
                EstadoEstadoP[estado][estadoPrev] =""+str(estadoMuestra)+"/"+str(sumEstado)
            # EstadoCanalF[estado][canal] =Fraction(int(EstadoCanalF[estado][canal])/len(indexEstados[estado]))
    print("Matriz valores despues de operar",EstadoEstadoP)

    return EstadoEstadoP

def allOps(estados_canales,numMuestras):
    print("\n*****MODO TODOS*****")
    #Almacena los indices de los estados, para reutilizarlos en el calculo de las otras matrices de estados
    indexEstados = {muestra: [] for muestra in muestrasBase}
    EstadoCanalF = {estados: {canal: 0 for canal in estados_canales.keys()} for estados in muestrasBase}
    EstadoEstadoF = {estado: {estado: 0 for estado in muestrasBase} for estado in muestrasBase}
    EstadoCanalP = {estados: {canal: 0 for canal in estados_canales.keys()} for estados in muestrasBase}
    EstadoEstadoP = {estados: {estado: 0 for estado in muestrasBase} for estados in muestrasBase}

    print("\nMatriz valores iniciales")
    print("EstadoCanalF:",EstadoCanalF)
    print("EstadoCanalP:",EstadoCanalP)
    print("EstadoEstadoF:",EstadoEstadoF)
    print("EstadoEstadoP:",EstadoEstadoP)
    
    # Itera por cada una de las muestras
    for time in range(numMuestras):
        # Añade el index, en el que un estado posible aparece en la muestra
        actual = getEstado(estados_canales,time)
        indexEstados[actual].append(time)
        # print("Estoy en la iteracion",time+1)
        # print("EL estado actual es", actual)
        if(time==0):
            proxEstado = getEstado(estados_canales,time+1)
            EstadoEstadoF[actual][proxEstado] += 1
            for canal in estados_canales.keys():
                proxEstadoCanal = estados_canales[canal][time+1]
                EstadoCanalF[actual][canal] += int(proxEstadoCanal)
            
        elif(time==numMuestras-1):
            prevEstado=getEstado(estados_canales,time-1)
            EstadoEstadoP[actual][prevEstado] += 1
            for canal in estados_canales.keys():
                prevEstadoCanal= estados_canales[canal][time-1]
                EstadoCanalP[actual][canal] += int(prevEstadoCanal)
        else:
            proxEstado=getEstado(estados_canales,time+1)
            EstadoEstadoF[actual][proxEstado] += 1
            prevEstado=getEstado(estados_canales,time-1)
            EstadoEstadoP[actual][prevEstado] += 1

            for canal in estados_canales.keys():
                proxEstadoCanal= estados_canales[canal][time+1]
                EstadoCanalF[actual][canal] += int(proxEstadoCanal)
                prevEstadoCanal= estados_canales[canal][time-1]
                EstadoCanalP[actual][canal] += int(prevEstadoCanal)

    print("\nMatriz valores conteo")
    print("Indexes",indexEstados)
    print("EstadoCanalF:",EstadoCanalF)
    print("\nEstadoCanalP:",EstadoCanalP)
    print("\nEstadoEstadoF:",EstadoEstadoF)
    print("\nEstadoEstadoP:",EstadoEstadoP)

    # Calcular las probabilidades dividiendo por el número de coincidencias del estado actual
    canales= list(estados_canales.keys())
    for estadoi in muestrasBase:
        # print("\nEvaluando para estado actual",estadoi)
        sumEstado=len(indexEstados[estadoi])
        # print("con apariciones en",indexEstados[estadoi])
        for canal in canales:
            # print("Evaluando para el canal",canal)
            estadoEvalF=EstadoCanalF[estadoi][canal]
            # print("estado en proximo",estadoEvalF)
            estadoEvalP=EstadoCanalP[estadoi][canal]
            # print("estado en previo",estadoEvalP)

            if(sumEstado==0):
                # print("Entro por divisor 0")
                EstadoCanalF[estadoi][canal]="Indefinido"
                EstadoCanalP[estadoi][canal]="Indefinido"
            # Por si el dividendo es 0
            elif(estadoEvalF==0 and estadoEvalP==0):
                # print("Entro por dividendo 0  (1)")
                EstadoCanalF[estadoi][canal]=str(0)
                # print("Entro por dividendo 0  (2)")
                EstadoCanalP[estadoi][canal]=str(0)

            elif(estadoEvalF==0):
                # print("Entro por dividendo 0  (1)")
                EstadoCanalF[estadoi][canal]=str(0)
                EstadoCanalP[estadoi][canal] =""+str(estadoEvalP)+"/"+str(sumEstado)
            elif(estadoEvalP==0):
                # print("Entro por dividendo 0  (2)")
                EstadoCanalP[estadoi][canal]=str(0)
                EstadoCanalF[estadoi][canal] =""+str(estadoEvalF)+"/"+str(sumEstado)
            # Por si la dicision es exacta 
            elif(estadoEvalF==sumEstado and estadoEvalP==sumEstado):
                EstadoCanalF[estadoi][canal]=str(int(estadoEvalF/sumEstado))
                EstadoCanalP[estadoi][canal]=str(int(estadoEvalP/sumEstado))
            elif(estadoEvalF==sumEstado):
                EstadoCanalF[estadoi][canal]=str(int(estadoEvalF/sumEstado))
                EstadoCanalP[estadoi][canal] =""+str(estadoEvalP)+"/"+str(sumEstado)
            elif(estadoEvalP==sumEstado):
                EstadoCanalP[estadoi][canal]=str(int(estadoEvalP/sumEstado))
                EstadoCanalF[estadoi][canal] =""+str(estadoEvalF)+"/"+str(sumEstado)
            # Por si la division no es exacta
            else:
                # print("***Estructurar fraccionarios***")
                # Descomentar si se desea fracciones simplificadas
                # estadoMuestra,sumEstado=simpFraccion(estadoMuestra,sumEstado) 

                EstadoCanalF[estadoi][canal] =""+str(estadoEvalF)+"/"+str(sumEstado)
                EstadoCanalP[estadoi][canal] =""+str(estadoEvalP)+"/"+str(sumEstado)
            # print("EstadoCanalF en este caso:",EstadoCanalF[estadoi][canal])
            # print("EstadoCanalP en este caso:",EstadoCanalP[estadoi][canal])
        

        for estadoj in muestrasBase:
            estadoEvalF=EstadoEstadoF[estadoi][estadoj]
            estadoEvalP=EstadoEstadoP[estadoi][estadoj]

            if(sumEstado==0):
                EstadoEstadoF[estadoi][estadoj]="Indefinido"
                EstadoEstadoP[estadoi][estadoj]="Indefinido"
            # Por si el dividendo es 0
            elif(estadoEvalF==0 and estadoEvalP==0):
                EstadoEstadoF[estadoi][estadoj]=str(0)
                EstadoEstadoP[estadoi][estadoj]=str(0)
            elif(estadoEvalF==0):
                EstadoEstadoF[estadoi][estadoj]=str(0)
                EstadoEstadoP[estadoi][estadoj] =""+str(estadoEvalP)+"/"+str(sumEstado)
            elif(estadoEvalP==0):
                EstadoEstadoP[estadoi][estadoj]=str(0)
                EstadoEstadoF[estadoi][estadoj] =""+str(estadoEvalF)+"/"+str(sumEstado)
            # Por si la dicision es exacta
            elif(estadoEvalF==sumEstado and estadoEvalP==sumEstado):
                EstadoEstadoF[estadoi][estadoj]=str(int(estadoEvalF/sumEstado))
                EstadoEstadoP[estadoi][estadoj]=str(int(estadoEvalP/sumEstado))
            elif(estadoEvalF==sumEstado):
                EstadoEstadoF[estadoi][estadoj]=str(int(estadoEvalF/sumEstado))
                EstadoEstadoP[estadoi][estadoj] =""+str(estadoEvalP)+"/"+str(sumEstado)
            elif(estadoEvalP==sumEstado):
                EstadoEstadoP[estadoi][estadoj]=str(int(estadoEvalP/sumEstado))
                EstadoEstadoF[estadoi][estadoj] =""+str(estadoEvalF)+"/"+str(sumEstado)
            # Por si la division no es exacta


            
            else:
                # Descomentar si se desea fracciones simplificadas
                # estadoMuestra,sumEstado=simpFraccion(estadoMuestra,sumEstado) 

                EstadoEstadoF[estadoi][estadoj] =""+str(estadoEvalF)+"/"+str(sumEstado)
                EstadoEstadoP[estadoi][estadoj] =""+str(estadoEvalP)+"/"+str(sumEstado)
            # EstadoEstadoF[estadoi][estadoj] =Fraction(int(EstadoEstadoF[estadoi][estadoj])/len(indexEstados[estadoi]))
            # EstadoEstadoP[estadoi][estadoj] =Fraction(int(EstadoEstadoP[estadoi][estadoj])/len(indexEstados[estadoi]))
    # print("\nMatriz valores despues de iterar")
    # print("EstadoCanalF:",EstadoCanalF)
    # print("\nEstadoCanalP:",EstadoCanalP)
    # print("\nEstadoEstadoF:",EstadoEstadoF)
    # print("\nEstadoEstadoP:",EstadoEstadoP)

    return EstadoCanalF, EstadoEstadoF, EstadoCanalP, EstadoEstadoP


#MENÚ QUE GENERA LOS ESTADOS ALEATORIOS
def menuGenerarEstadosAleatorios():
    num_canales = int(input("Ingresa el numero de canales: "))
    generar_muestras(num_canales)
    num_muestras = int(input("Ingresa el numero de muestras: "))

    estados_aleatorios = generar_estados_aleatorios(num_canales, num_muestras)

    print("\nEstados generados aleatoriamente:")
    mostrar_estados(estados_aleatorios)

    #Prueba todos
    matrizEstadoCanalF, matrizEstadoEstadoF, matrizEstadoCanalP, matrizEstadoEstadoP = allOps(estados_aleatorios,num_muestras)

    #Punto 1
    # Calcular la matriz de probabilidades basada en los estados generados aleatoriamente
    # matrizEstadoCanalF, indexEstados = calcular_matriz_EstadoCanalF(estados_aleatorios,num_muestras)
    graphMatriz(matrizEstadoCanalF,"+")

    #Punto 2
    # matrizEstadoEstadoF = generar_matriz_EstadoEstadoF(indexEstados)
    graphMatriz(matrizEstadoEstadoF,"+")

    
    #Punto 3
    # Calcular la matriz de probabilidades previas basada en los estados generados aleatoriamente Punto 3
    # matrizEstadoCanalP = calcular_matriz_EstadoCanalP(estados_aleatorios,num_muestras,indexEstados)
    graphMatriz(matrizEstadoCanalP,"-")

    # punto 4
    # matrizEstadoEstadoP = generar_matriz_EstadoEstadoP(indexEstados)
    graphMatriz(matrizEstadoEstadoP,"-")



    
#DATOS DE PRUEBA
sampleData={
    "A":["0","1","1","0","1","1","0","0","0","1","1","0","1","0","1","0","1","0","1","0","1","0","1","0","1","1","0","0","0","1"],
    "B":["0","0","0","1","1","0","1","0","1","0","1","0","1","0","1","1","0","1","1","0","1","1","0","1","1","1","1","0","0","0"],
    "C":["0","1","0","1","0","1","0","1","0","1","1","0","1","1","0","1","1","1","1","0","1","0","1","0","1","0","1","0","1","0"]
}

# FUNCIÓN QUE MUESTRA LOS ESTADOS DE PRUEBA DE SAMPLEDATA
def mostrar_estados_prueba():
    print("Mostrando estados:")
    for key, value in sampleData.items():
        print(f"{key}: {value}")

    num_canales = len(sampleData)
    generar_muestras(num_canales)
    num_muestras = len(sampleData[list(sampleData.keys())[0]])

    #Prueba todos
    matrizEstadoCanalF, matrizEstadoEstadoF, matrizEstadoCanalP, matrizEstadoEstadoP = allOps(sampleData,num_muestras)

    #Punto 1
    # Calcular la matriz de probabilidades basada en los estados generados aleatoriamente
    # matrizEstadoCanalF, indexEstados = calcular_matriz_EstadoCanalF(sampleData,num_muestras)
    graphMatriz(matrizEstadoCanalF,"+")


    #Punto 2
    # matrizEstadoEstadoF = generar_matriz_EstadoEstadoF(indexEstados)
    graphMatriz(matrizEstadoEstadoF,"+")

    
    #Punto 3
    # Calcular la matriz de probabilidades previas basada en los estados generados aleatoriamente Punto 3
    # matrizEstadoCanalP = calcular_matriz_EstadoCanalP(sampleData,num_muestras,indexEstados)
    graphMatriz(matrizEstadoCanalP,"-")

    # punto 4
    # matrizEstadoEstadoP = generar_matriz_EstadoEstadoP(indexEstados)
    graphMatriz(matrizEstadoEstadoP,"-")

################ MENÚ PRINCIPAL ###################
def menuPrincipal():
    while True:
        print("\n\n\tMenu Principal")
        print("1) Generar estados aleatorios")
        print("2) Usar datos de prueba")
        print("3) Salir")

        opcion = int(input("Ingresa una opcion: "))

        if opcion == 1:
            menuGenerarEstadosAleatorios()
        elif opcion == 2:
            mostrar_estados_prueba()
        elif opcion == 3:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción válida.")

# Llamamos al menú principal
if __name__ == "__main__":
    menuPrincipal()
