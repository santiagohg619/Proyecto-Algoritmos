import random

def formula(estado_futuro, estado_actual):
    
    return estado_futuro / estado_actual

def aplicar_formula(estado_futuro, estado_actual, canales):
    """
    Evalúa las condiciones y aplica la fórmula si es necesario.
    
    Parámetros:
    estado_futuro (int): El estado futuro que es el numerador en la fórmula.
    estado_actual (int): El estado actual que es el denominador en la fórmula.
    numero_canales (int): El número de canales del sistema.
    
    Retorna:
    resultado (float): El resultado de aplicar la fórmula o None si la fórmula no se aplica.
    """
    # Primera condición: Si el estado futuro y el estado actual son iguales al número de canales, no se aplica la fórmula.
    if estado_futuro == canales and estado_actual == canales:
        return None
    
    # Segunda condición: Si el estado futuro es menor o igual al número de canales y el estado actual es menor al número de canales, se aplica la fórmula.
    if estado_futuro <= canales and estado_actual < canales:
        # Aquí aplicarías la fórmula específica que necesitas
        resultado = # La fórmula que necesitamos aplicar en este caso
        return resultado
    
    # Si ninguna de las condiciones anteriores se cumple, no se aplica la fórmula.
    return None

# Ejemplo de uso:
estado_futuro = 3
estado_actual = 2
numero_canales = 4
resultado = aplicar_formula(estado_futuro, estado_actual, numero_canales)
if resultado is not None:
    print("El resultado de aplicar la fórmula es:", resultado)
else:
    print("No se aplica la fórmula.")


def dividir_y_calcular_probabilidades(estados_globales, probabilidades_transicion, numero_canales):
    """
    Se divide el sistema global en dos subsistemas de manera aleatoria y calcula la probabilidad de cada uno.
    
    Parámetros:
    estados_globales (list): Lista de estados en el sistema global.
    probabilidades_transicion (dict): Diccionario con las probabilidades de transición para cada estado.
    
    Retorna:
    probabilidad_subsistema_1 (float), probabilidad_subsistema_2 (float): Probabilidades de los subsistemas.
    """
    # Mezclar y dividir los estados
    random.shuffle(estados_globales)
    mitad = len(estados_globales) // 2
    subsistema_1 = estados_globales[:mitad]
    subsistema_2 = estados_globales[mitad:]
    
    # Calcular la probabilidad para cada subsistema
    probabilidad_subsistema_1 = 1
    for estado in subsistema_1:
        probabilidad_subsistema_1 *= probabilidades_transicion[estado]
    
    probabilidad_subsistema_2 = 1
    for estado in subsistema_2:
        probabilidad_subsistema_2 *= probabilidades_transicion[estado]
    
    return probabilidad_subsistema_1, probabilidad_subsistema_2

    # Ahora, aplicamos la fórmula a cada subsistema si es necesario
    resultado_subsistema_1 = aplicar_formula(probabilidad_subsistema_1, probabilidad_subsistema_1, numero_canales)
    resultado_subsistema_2 = aplicar_formula(probabilidad_subsistema_2, probabilidad_subsistema_2, numero_canales)
    
    return resultado_subsistema_1, resultado_subsistema_2

# Ejemplo de uso:
estados = ['Estado1', 'Estado2', 'Estado3', 'Estado4', 'Estado5']
probabilidades = {
    'Estado1': 0.1,
    'Estado2': 0.2,
    'Estado3': 0.3,
    'Estado4': 0.4,
    'Estado5': 0.5
}
numero_canales = 4
resultados = dividir_y_calcular_probabilidades(estados, probabilidades, numero_canales)
print("Resultados de los subsistemas:", resultados)