#Librerias:
from tabulate import tabulate
from biparts import allBiParticiones
from scipy.stats import wasserstein_distance
import numpy as np
import time
inicio = time.time()

def graphMatriz(matriz, opc):
    if opc == "+":
        titulosColumnas = ["Estado//T+1"]
    elif opc == "-":
        titulosColumnas = ["Estado//T-1"]
    otrosTitulos = matriz[list(matriz.keys())[0]].keys()
    titulosColumnas.extend(otrosTitulos)
    table = [[key] + [matriz[key][column] for column in titulosColumnas[1:]] for key in matriz.keys()]
    print(tabulate(table, titulosColumnas, tablefmt="fancy_grid"))

tiempos = {"Actual":dict(),"Futuro":list()}
canalesBase = ["a","b","c"]

#Original
"""
sampleData={
    '000': {'000': 1, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 0},
    '001': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 1, '101': 0, '110': 0, '111': 0},
    '010': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 1, '110': 0, '111': 0},
    '011': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 1, '110': 0, '111': 0},
    '100': {'000': 0, '001': 1, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 0},
    '101': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 1},
    '110': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 1, '101': 0, '110': 0, '111': 0},
    '111': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 1, '111': 0}
    }
"""

#Sustentación
sampleData = {
    '000': {'000': 1, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 0},
    '001': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 1, '101': 0, '110': 0, '111': 0},
    '010': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 1, '110': 0, '111': 0},
    '011': {'000': 0, '001': 1, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 0},
    '100': {'000': 0, '001': 1, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 0},
    '101': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 1},
    '110': {'000': 0, '001': 0, '010': 0, '011': 0, '100': 0, '101': 0, '110': 0, '111': 0},
    '111': {'000': 0, '001': 0, '010': 0, '011': 1, '100': 0, '101': 0, '110': 0, '111': 0}
    }


def menuDivision(data=sampleData, canales=canalesBase):   
    #Corregir para listas vacias
    print("\n\nLa matriz original es")
    graphMatriz(data,"+")
    print("\n**Menu de particiones**")
    print(tiempos)
    print("Los canales disponibles para realizar las particiones son: ", canales)
    for tiempo in tiempos:
        print("\nIngrese los canales de la particion {}".format(tiempo)+" Ejemplo: a,b,c o b,c o a,c")
        part = input().lower()
        part = part.split(",")
        for canal in part:
            if canal not in canales:
                print("**El canal {} no existe**".format(canal))
                menuDivision(sampleData, canalesBase)
            if tiempo == "Actual":
                while True:
                    print("ingrese el valor actual para el canal {}".format(canal))
                    val = input()
                    if val not in ["0","1"]:
                        print("\nEl valor debe ser 0 o 1")
                    else:
                        tiempos[tiempo][canal]=val
                        break
            else:
                tiempos[tiempo].append(canal)
    print("\n\nTiempos iniciales: ", tiempos)
    print("\nDesea realizar comprobaciones de distancia entre particiones(s/n)?")
    op=input()
    if op == "s":    
        final(data, canales)
    else:
        printDataDivision(data, canales, list(tiempos["Actual"].keys()), tiempos["Futuro"])
        print("\nTiempo empleado: ", fin - inicio ,"\n")

#Código a medir 
time.sleep(1)
def final(data,canales):
    biPartActuales, biPartFuturo = allBiParticiones(tiempos)
    #calculo de original
    print("***Se mirara el original**")
    original = printDataDivision(data, canales, list(tiempos["Actual"].keys()), tiempos["Futuro"])
    print("\n\n")
    matFinal = {}
    for i in range(len(biPartActuales)):
        for j in range(len(biPartFuturo)):
            for ii in range(len(biPartActuales[i])):
                referencias = []
                preStr = ""
                for jj in range(len(biPartFuturo[j])):
                    if (biPartActuales[i][ii] == []) and (biPartFuturo[j][jj] == []):
                        continue
                    print("Para el actual", biPartActuales[i][ii])
                    preStr += str(biPartActuales[i][ii])
                    print("Para el futuro", biPartFuturo[j][jj])
                    preStr += str(biPartFuturo[j][jj])
                    referencia = printDataDivision(data, canales, biPartActuales[i][ii], biPartFuturo[j][jj])
                    # print("La referencia dio:",referencia,"\n\n")
                    referencias.append(referencia)
                    preStr += " // "
                preStr = preStr[:-3]
                temp = []
                for element in referencias:
                    preList = []
                    for key in element:
                        for subkey in element[key]:
                            preList.append(element[key][subkey])
                    temp.append(preList)
                # print("Datos de temp:", temp)
                matFinal[preStr] = multpMatriz(temp)
                # print("Tras Multiplicar:",matFinal[preStr])
                checkEmd(original.copy(),matFinal.copy(),preStr)


def checkEmd(original, matFinal, preStr):
    # print("Original:",original[list(original.keys())[0]])
    # print("Matfinal:",matFinal[preStr])
    if len(list(original[list(original.keys())[0]].keys())) == len(list(matFinal[preStr].keys())):
        print("\nComparacion de distancia con la distrinucion compuesta: ", preStr)
        keysA = list(original[list(original.keys())[0]].keys())
        tempA = []
        keysB = list(matFinal[preStr].keys())
        tempB = []
        for i in range(len(keysA)):
            tempA.append(original[list(original.keys())[0]][keysA[i]])
            tempB.append(matFinal[preStr][keysB[i]])    
        print("valores previos:", tempA)
        print("valores previos:", tempB)
        # Calculamos la distancia EMD entre las dos distribuciones
        distancia_emd = wasserstein_distance(tempA, tempB)
        # Mostramos el resultado
        print(f'Distancia EMD: {distancia_emd}')
        print("\n\n\n")
fin = time.time()

def printDataDivision(data,canales,listActual,listFuturo):
    actCoincidencias = []
    elmCoincidencias = []
    futCoincidencias = {}

    #Por los identificadores de canales en actual
    for i in range(len(listActual)):
        lAct = listActual[i]
        #Valor de de referencia en el canal
        canalEstAct = tiempos["Actual"][lAct]
        if not(canalEstAct == None):
            indexT = canales.index(lAct)
            # Si es la primera coincidencia
            if i == 0:
                #Por cada entrada en la matriz
                for entry in data:
                    if entry[indexT] == canalEstAct:
                        # print("Entradas que parcialmente coinciden:",entry)
                        actCoincidencias.append(entry)
            else:
                # print("Estado actCoincidencias:",actCoincidencias)
                for entry in actCoincidencias:
                    # print("Se esta verificando que la entrada {} tenga un {} en la posicion {}".format(entry,canalEstAct,indexT+1))
                    if not(entry[indexT] == canalEstAct):
                        #print("No cumplio")
                        elmCoincidencias.append(entry)
    #Ciclo para eliminar valores invalidos
    for el in elmCoincidencias:
        if el in actCoincidencias:
            actCoincidencias.remove(el)
    # print("Entradas que coinciden:",actCoincidencias)

    #Por los identificadores de canales en futuro
    for entry in actCoincidencias:
        for i in range(len(listFuturo)):
            futCoincidencias[listFuturo[i]] = {"0":[], "1":[]}
            for value in data[entry]:
                indexEval = canales.index(listFuturo[i])
                for bin in ["0", "1"]:
                    if value[indexEval] == bin:
                        futCoincidencias[listFuturo[i]][bin].append(value)           
    # print("valores por entrada:",futCoincidencias)

    return operProbs(actCoincidencias,futCoincidencias,data)

def auxOperProbs(data, actList, dataEntrada):
    cero = []
    uno = []
    for act in actList:
        # print("act:",act)
        for fut in dataEntrada:
            # print("fut:",fut)
            for value in dataEntrada[fut]:
                # print("value:",value)
                valItem = data[act][value]
                if type(valItem) == str:
                    valItem = eval(valItem)
                if fut == "0":
                    cero.append(valItem)
                else:
                    uno.append(valItem)
    #print("cero:",cero)
    #print("uno:",uno)

    cero = sum(cero*4)/len(cero)
    uno = sum(uno*4)/len(uno)
    return [cero, uno]

def multpMatriz(listas):
    # Inicializamos el diccionario para almacenar los resultados
    resultados = {}
    # Calculamos el número total de combinaciones posibles
    num_combinaciones = 1
    for lista in listas:
        num_combinaciones *= len(lista)
    # print("num_combinaciones:",num_combinaciones)
    # Generamos todas las combinaciones de índices manualmente
    for i in range(num_combinaciones):
        # print("ha entrado")
        clave = ''
        resultado = 1
        # Calcular los índices para cada lista
        for j in range(len(listas)):
            # print("j:",j)
            lista = listas[j]
            # print("lista:",lista)
            indice = (i // (len(lista) ** j)) % len(lista)
            # print("indice:",indice)
            clave += str(indice)
            # print("clave:",clave)
            resultado *= lista[indice]
        resultados[clave] = resultado
    return resultados

def operProbs(actlist, futList, data):
    matFinal = {}
    auxStr = str(tiempos['Actual'])
    # print(auxStr)
    probsEntrada = {}
    for entrada in futList:
        probsEntrada[entrada] = auxOperProbs(data, actlist, futList[entrada])
    # print("debug:",probsEntrada)
    listProbsEntrada = []
    for key in probsEntrada:
        listProbsEntrada.append(probsEntrada[key])
    # print("zzz",listProbsEntrada)
    if len(listProbsEntrada) == 1:
        matFinal[auxStr] = {"0":listProbsEntrada[0][0], "1":listProbsEntrada[0][1]}
        # print(matFinal)
        graphMatriz(matFinal, "+")
    else:
        matFinal[auxStr] = multpMatriz(listProbsEntrada)
        # print(matFinal)
        graphMatriz(matFinal, "+")
    return matFinal

def menu():
    menuDivision(sampleData, canalesBase)

if __name__ == "__main__":
    menu()