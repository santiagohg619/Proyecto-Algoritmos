
def genBipart(lista):
    if not lista:
        return [([], [])]  # Lista vacía, devuelve una bipartición con dos listas vacías

    primer_elemento = lista[0]
    restante = lista[1:]

    # Recursivamente generamos todas las biparticiones del resto de la lista
    restantes_biparticiones = genBipart(restante)

    # Para cada bipartición generada recursivamente, tenemos dos opciones:
    # 1. Incluir el primer elemento en la primera parte de la bipartición
    # 2. Incluir el primer elemento en la segunda parte de la bipartición

    todas_biparticiones = []
    for parte1, parte2 in restantes_biparticiones:
        todas_biparticiones.append([[primer_elemento] + parte1, parte2])
        todas_biparticiones.append([parte1, [primer_elemento] + parte2])

    return todas_biparticiones

# # Ejemplo de uso
# mi_lista = ['a', 'c']
# mi_lista2 = ['a', 'b', 'c']


# biparticiones = genBipart(mi_lista)

# Mostramos los resultados



def allBiParticiones(tiempos):
    print(tiempos)
    print("\n\n***Entro a biparticiones***")
    listActual=list(tiempos["Actual"].keys())
    print("listActual",listActual)
    listFuturo=tiempos["Futuro"]
    print("listFuturo",listFuturo)

    biPartActuales=genBipart(listActual)
    print("actuales:")
    for biparticion in biPartActuales:
        print(biparticion)

    print("futuros")
    biPartFuturo=genBipart(listFuturo)
    for biparticion in biPartFuturo:
        print(biparticion)

    return biPartActuales, biPartFuturo

# allBiParticiones(None)
