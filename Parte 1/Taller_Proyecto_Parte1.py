"""
[---------------------------------------------------- MANUAL DE USO ----------------------------------------------------------]

REQUISITOS DEL SISTEMA: 
Python 3.x instalado en su computadora

LIBRERIAS NECESARIAS PARA EL FUNCIONAMIENTO: :

random: La biblioteca random es una biblioteca estándar de Python, 
por lo que no necesitas instalarla por separado. Ya está disponible en 
cualquier instalación estándar de Python.

math.gcd: De nuevo, math.gcd es parte de la biblioteca estándar de Python 
y no requiere instalación adicional. Puedes importarlo directamente como lo 
hiciste en tu código.

tabulate: Para instalar la biblioteca tabulate, puedes utilizar el gestor de paquetes pip, 
que es la forma estándar de instalar paquetes externos en Python. Abre una terminal o línea 
de comandos y ejecuta el siguiente comando:

-------------------------------------------------------------------------------------------------------------------------------

COMANDO PARA INSTALACIÓN DE LIBRERIAS:
Instalar bibliotecas en Python es un proceso común y esencial cuando trabajas en proyectos que 
requieren funcionalidades específicas proporcionadas por bibliotecas externas. Aquí tienes un 
proceso general para instalar bibliotecas en Python:


1.Verificar la instalación de Python: Antes de comenzar, asegúrate de tener Python instalado en 
tu sistema. Abre una terminal o línea de comandos y ejecuta el siguiente comando para verificar 
la versión de Python instalada:
   ```
   python --version
   ```
Si no tienes Python instalado, descárgalo desde el sitio web oficial de Python (https://www.python.org/) 
e instálalo siguiendo las instrucciones proporcionadas para tu sistema operativo.

2. Instalar pip (si no está instalado): Pip es el gestor de paquetes de Python y se utiliza para 
instalar bibliotecas externas. Asegúrate de tener pip instalado en tu sistema. Algunas versiones 
de Python lo incluyen de forma predeterminada. Para verificar si pip está instalado, ejecuta:
   ```
   pip --version
   ```
Si no está instalado, puedes seguir las instrucciones para instalar pip en el sitio web oficial 
de Python: https://pip.pypa.io/en/stable/installation/

3. Instalar bibliotecas con pip: Una vez que tienes Python y pip configurados, puedes instalar 
bibliotecas externas con el comando `pip install`. Para instalar una biblioteca específica, 
ejecuta el siguiente comando:
   ```
   pip install nombre_de_la_biblioteca
   ```
Reemplaza "nombre_de_la_biblioteca" con el nombre real de la biblioteca que deseas instalar. 
Por ejemplo, si deseas instalar la biblioteca `requests`, ejecutarías:
   ```
   pip install requests
   ```
Pip descargará e instalará automáticamente la biblioteca y sus dependencias.

4. Verificar la instalación: Después de la instalación, puedes verificar que la biblioteca 
se haya instalado correctamente. Abre un entorno de Python o un script y ejecuta el siguiente comando:
   ```python
   import nombre_de_la_biblioteca
   ```
Reemplaza "nombre_de_la_biblioteca" con el nombre real de la biblioteca que instalaste. 
Si no se produce ningún error, significa que la biblioteca se ha instalado correctamente y 
puedes comenzar a usarla en tus proyectos.

-------------------------------------------------------------------------------------------------------------------------------

FUNCIONAMIENTO DEL CÓDIGO:

### 1. Generar Estados Aleatorios ###

Al seleccionar la opción "Generar estados aleatorios" en el menú principal (opción 1), 
el programa generará estados aleatorios para n canales especificados por el usuario. Siga estos pasos:

   1. Ingrese el número de canales deseado.
   2. Ingrese el número de muestras que desea generar.

El programa generará estados aleatorios para los canales y calculará varias matrices de probabilidad 
basadas en estos estados.

-------------------------------------------------------------------------------------------------------------------------------

### 2. Usar Datos de Prueba ###

Al seleccionar la opción "Usar datos de prueba" en el menú principal (opción 2), el programa mostrará 
un conjunto de estados de prueba predefinidos llamados `sampleData`. Estos estados de prueba se utilizan 
para calcular matrices de probabilidad basadas en estados ya definidos. 

--------------------------------------------------------------------------------------------------------------------------------

### 3. Salir ###

La opción "Salir" (opción 3) cierra el programa.

--------------------------------------------------------------------------------------------------------------------------------

### Visualización de Matrices ###

El código genera varias matrices de probabilidad, como EstadoCanalF y EstadoEstadoF, y las 
muestra en formato tabular utilizando la biblioteca `tabulate`. Las matrices se presentan de manera legible en la consola.

[--------------------------------------------------------------------------------------------------------------------------------]

##############################################################################################################################

[------------------------------------------------------- MANUAL DE USUARIO ----------------------------------------------------------]

### Menú Principal ###

Al iniciar el programa, te encontrarás en el "Menú Principal". Aquí encontrarás las siguientes opciones:
1. Generar Estados Aleatorios: Esta opción te permite generar estados aleatorios para los canales y 
calcular las matrices de probabilidad correspondientes basadas en esos estados.

2. Usar Datos de Prueba: Esta opción te muestra un conjunto de estados de prueba predefinidos llamados 
`sampleData`. Estos estados se utilizan para calcular matrices de probabilidad basadas en estados ya definidos.

3. Salir: Esta opción cierra el programa.

### Generar Estados Aleatorios ###

Cuando elijas la opción "Generar Estados Aleatorios" (opción 1), el programa te pedirá que ingreses algunos detalles:
- Número de Canales: Debes especificar el número de canales para los cuales deseas generar estados aleatorios.

**Número de Muestras**: Luego, debes indicar cuántas muestras aleatorias deseas generar.

### Usar Datos de Prueba ###

Si eliges la opción "Usar Datos de Prueba" (opción 2), el programa mostrará un conjunto de estados de prueba predefinidos llamados `sampleData`. Estos estados de prueba ya están definidos en el código y se utilizan para calcular matrices de probabilidad basadas en esos estados.

### Visualización de Matrices ###

El programa calculará varias matrices de probabilidad, como EstadoCanalF, EstadoEstadoF, EstadoCanalP y EstadoEstadoP, en función de los estados generados o los datos de prueba. Estas matrices se mostrarán en formato tabular en la consola para facilitar su visualización y análisis.

### Salir del Programa ###

Si deseas salir del programa en cualquier momento, selecciona la opción "Salir" (opción 3) en el menú principal.

Este manual de usuario te proporciona una visión general de cómo utilizar el programa para generar estados aleatorios y calcular matrices de probabilidad basadas en esos estados. ¡Disfruta explorando las funcionalidades y analizando las matrices calculadas!
"""

####################################################################################################################################################################################################################################################################################################
# ANÁLISIS Y DISEÑO DE ALGORITMOS
# MANUELA ZULUAGA CARDONA
# SANTIAGO HOYOS GÓMEZ
# 2023-2
####################################################################################################################################################################################################################################################################################################

import random
"""
    La biblioteca random proporciona funciones para generar números aleatorios. 
    En este código, se utiliza para seleccionar estados aleatorios ("0" o "1") 
    para cada canal en la función generar_estados_aleatorios. Esto es útil para 
    simular estados aleatorios en un sistema de canales y generar datos de prueba.
"""
# from fractions import Fraction

from math import gcd
"""
    La función gcd de la biblioteca math se utiliza para calcular el máximo 
    común divisor (MCD) de dos números. En este código, se usa en la función 
    simpFraccion para simplificar fracciones. El MCD se emplea para reducir 
    una fracción a su forma más simple, lo que puede ser útil en cálculos de 
    probabilidades.
"""
from tabulate import tabulate
"""
    La biblioteca tabulate es utilizada para formatear y mostrar matrices 
    y tablas de datos en un formato tabular en la consola. Se utiliza en la 
    función graphMatriz para presentar de manera organizada las matrices de 
    probabilidades calculadas en el programa. Esto hace que sea más fácil 
    para el usuario comprender y analizar los resultados al imprimirlos en 
    una tabla bien estructurada.
"""

# Recordar comparar con valores string no enteros
# Descomentar si se desea fracciones simplificadas
# estadoCanal,sumEstado=simpFraccion(estadoCanal,sumEstado) en la funcion calcular_matriz_EstadoCanalF

muestrasBase = []
#Genera las 2^n posibilidades de n canales
def generar_muestras(numCanales):
    """
        Esta función genera todas las posibles combinaciones de estados para los canales. 
        El número de canales y sus estados posibles se determinan en función del argumento numCanales. 
        Cada combinación se almacena en una lista llamada muestrasBase.
    """
    for i in range(2 ** numCanales):
        num = format(i, f'0{numCanales}b')
        muestrasBase.append(num)

def generar_estados_aleatorios(num_canales, num_muestras):
    """
        Esta función genera estados aleatorios para los canales. Debes proporcionar 
        el número de canales (num_canales) y el número de muestras (num_muestras) que deseas generar. 
        Los estados se eligen de manera aleatoria entre "0" y "1" para cada canal, y se almacenan en un 
        diccionario llamado estados_generados, donde cada clave representa un canal y su valor es una lista 
        de estados aleatorios.
    """
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
    """
        Esta función muestra en la consola los estados generados en el diccionario estados. 
        Muestra cada canal y sus estados correspondientes.
    """
    for canal, estados_canal in estados.items():
        print(f"{canal}:", estados_canal)

# Junta los datos de los n canales en un solo string
def getEstado(canalesData, iteracion):
    """
        Esta función toma los datos de estados de múltiples canales y los une en un 
        solo string en función de la iteración especificada. Es útil para obtener el estado 
        en un momento específico en el tiempo.
    """
    res = ""
    for keys in canalesData:
        res += str(canalesData[keys][iteracion])
    return res

def simpFraccion(dividendo, divisor):
    """
        Esta función simplifica una fracción dividiendo el dividendo y el divisor por su máximo común divisor (MCD).
    """
    #Halla el maximo comun divisor
    mcd=gcd(dividendo,divisor)

    if mcd!=1:
        dividendo=dividendo//mcd
        divisor=divisor//mcd
    
    return dividendo, divisor

def graphMatriz(matriz, opc):
    """
        Esta función imprime una matriz en formato tabular utilizando la biblioteca tabulate. 
        El argumento opc se utiliza para determinar si la matriz representa estados actuales, 
        anteriores o pasados.

    """
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
    """
        Esta función calcula la matriz de probabilidades de los estados futuros de los canales basada en 
        los estados actuales. Devuelve la matriz de probabilidades y un diccionario que almacena los índices 
        de los estados en las muestras.
    """
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

#Punto 2:
def generar_matriz_EstadoEstadoF(indexsEstados):
    """
        Esta función calcula la matriz de transición de estados futuros basada en 
        los estados actuales y los índices de los estados en las muestras. Devuelve esta 
        matriz de transición de estados futuros.
    """
    # Inicializar la matriz de probabilidades previas con ceros
    EstadoEstadoF = {estado: {estado: 0 for estado in muestrasBase} for estado in muestrasBase}
    print("Matriz inicial", EstadoEstadoF)
    
    #Iteracion n*n de estados 
    for estado in muestrasBase:
        for estadoNext in muestrasBase:
            for index in indexsEstados[estado]:
                # print("actual",index)
                for indexNext in indexsEstados[estadoNext]:
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
            sumEstado= len(EstadoEstadoF[estado])
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

#Punto 3:
def calcular_matriz_EstadoCanalP(estados_canales,numMuestras,indexEstados):
    """
        Esta función calcula la matriz de transición de estados actuales basada en los estados pasados 
        y los estados posibles. Devuelve esta matriz de transición de estados actuales.
    """
    EstadoCanalP = {estados: {canal: 0 for canal in estados_canales.keys()} for estados in muestrasBase}
    print("Matriz Inicial",EstadoCanalP)
    
    # Itera por cada una de las muestras
    for time in range(1,numMuestras):
        temp = getEstado(estados_canales,time)
        # print("Ha entrado")
        for canal in estados_canales.keys():
            proxEstadoCanal= estados_canales[canal][time-1]
            EstadoCanalP[temp][canal] += int(proxEstadoCanal)

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

#Punto 4:
def generar_matriz_EstadoEstadoP(indexsEstados):
    """
        Esta función implementa un menú interactivo que permite al usuario ingresar 
        el número de canales y el número de muestras para generar estados aleatorios. Luego, 
        muestra las matrices calculadas y los resultados basados en esos estados.
    """
    # Inicializar la matriz de probabilidades previas con ceros
    EstadoEstadoP = {estado: {estado: 0 for estado in muestrasBase} for estado in muestrasBase}
    print("Matriz inicial", EstadoEstadoP)
    
    #Iteracion n*n de estados 
    for estado in muestrasBase:
        for estadoPrev in muestrasBase:
            for index in indexsEstados[estado]:
                # print("actual",index)
                for indexPrev in indexsEstados[estadoPrev]:
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
            sumEstado= len(EstadoEstadoP[estado])
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

#MENÚ QUE GENERA LOS ESTADOS ALEATORIOS
def menuGenerarEstadosAleatorios():
    num_canales = int(input("Ingresa el numero de canales: "))
    generar_muestras(num_canales)
    num_muestras = int(input("Ingresa el numero de muestras: "))
    #Llamado de la función generar_estados_aleatorios()
    estados_aleatorios = generar_estados_aleatorios(num_canales, num_muestras)
    #Mostrar:
    print("\nEstados generados aleatoriamente:")
    mostrar_estados(estados_aleatorios)

    #Punto 1
    # Calcular la matriz de probabilidades basada en los estados generados aleatoriamente
    matrizEstadoCanalF, indexEstados = calcular_matriz_EstadoCanalF(estados_aleatorios,num_muestras)
    graphMatriz(matrizEstadoCanalF,"+")

    #Punto 2
    matrizEstadoEstadoF = generar_matriz_EstadoEstadoF(indexEstados)
    graphMatriz(matrizEstadoEstadoF,"+")

    #Punto 3
    # Calcular la matriz de probabilidades previas basada en los estados generados aleatoriamente Punto 3
    matrizEstadoCanalP = calcular_matriz_EstadoCanalP(estados_aleatorios,num_muestras,indexEstados)
    graphMatriz(matrizEstadoCanalP,"-")

    # punto 4
    matrizEstadoEstadoP = generar_matriz_EstadoEstadoP(indexEstados)
    graphMatriz(matrizEstadoEstadoP,"-")

#DATOS DE PRUEBA
#Diccionario de datos:
sampleData = {
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

    #Punto 1
    # Calcular la matriz de probabilidades basada en los estados generados aleatoriamente
    matrizEstadoCanalF, indexEstados = calcular_matriz_EstadoCanalF(sampleData,num_muestras)
    graphMatriz(matrizEstadoCanalF,"+")

    #Punto 2
    matrizEstadoEstadoF = generar_matriz_EstadoEstadoF(indexEstados)
    graphMatriz(matrizEstadoEstadoF,"+")

    #Punto 3
    # Calcular la matriz de probabilidades previas basada en los estados generados aleatoriamente Punto 3
    matrizEstadoCanalP = calcular_matriz_EstadoCanalP(sampleData,num_muestras,indexEstados)
    graphMatriz(matrizEstadoCanalP,"-")

    # punto 4
    matrizEstadoEstadoP = generar_matriz_EstadoEstadoP(indexEstados)
    graphMatriz(matrizEstadoEstadoP,"-")

################ MENÚ PRINCIPAL ###################
def menuPrincipal():
    while True:
        print("[-----------------------------------------------------------------]")
        print("\n\n\tMenu Principal")
        print("1) Generar estados aleatorios")
        print("2) Usar datos de prueba")
        print("3) Salir")
        print("[-----------------------------------------------------------------]")
        print("")
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
menuPrincipal()