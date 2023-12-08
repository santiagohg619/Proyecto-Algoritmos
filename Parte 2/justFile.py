from chatTaller1 import allOps, graphMatriz, generar_muestras


def operar(channels_data, numMuestras):

    matrizEstadoCanalF, matrizEstadoEstadoF, matrizEstadoCanalP, matrizEstadoEstadoP = allOps(channels_data,numMuestras)

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



channels_data={}
contador=1
try:
    with open("./testfile.csv", 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if not(i==len(lines)-1):
                channel_data = lines[i][:-1].split(',')
            for element in channel_data:
                if element=='' or element not in ("0","1"):
                    print("Error por el elemento", element)
            channels_data[chr(64+contador)]= channel_data
            print(chr(64+contador),"\nchannel_data",channel_data)
            contador+=1
    print()
    print(channels_data)
    #return channels_data
    numMuestras=len(channels_data[list(channels_data.keys())[0]])
    generar_muestras(len(channels_data.keys()))
    operar(channels_data,numMuestras)
except FileNotFoundError:
    print("Archivo no encontrado.")
    




