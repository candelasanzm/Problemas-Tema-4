# FUNCIONES

def secuencias(a : list, b : list) -> tuple[int, list]:

    # Obtenemos las longitudes de las listas de entrada
    n = len(a)
    m = len(b)

    # Inicializamos la matriz con ceros
    matriz = []

    # Construir la matriz
    for i in range(n + 1):
        fila = []
        for j in range(m + 1):
            fila.append(0) # Cada posición se llena con 0
        matriz.append(fila)

    # Llenar la matriz haciendo uso de la programación dinámica
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]: # Si los elementos coinciden
                matriz[i][j] = matriz[ i- 1][j - 1] + 1 # Se incrementa el valor
            else:
                matriz[i][j] = max(matriz[i - 1][j], matriz[i][j - 1]) # Si no coinciden, se toma el máximo
    
    # Subsecuencia común más larga
    i = n
    j = m
    subsec = [] # Lista para almcenar la subsecuencia

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]: # Si hay coincidencia
            subsec.append(a[i - 1]) # Se añade el elemento
            i -= 1
            j -= 1
        elif matriz[i - 1][j] >= matriz[i][j - 1]: # Si el valor de arriba es mayor
            i -= 1 # Se mueve hacia arriba en la matriz
        else:
            j -= 1 # Se mueve hacia la izquierda

    subsec.reverse() # Se invierte la lista para obtener el orden correcto
    return matriz[n][m], subsec # Retorna la longitud y la subsecuencia


# CASOS DE PRUEBA
casos_prueba = [
    # Caso estándar
    ([0, 1, 1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 0, 1, 0, 0, 1]),
    
    # Caso con una única coincidencia
    ([1, 2, 3], [4, 5, 1]),
    
    # Caso sin subsecuencia común
    ([0, 0, 0], [1, 1, 1]),
    
    # Caso con valores repetitivos
    ([1, 1, 1, 1, 1, 2, 1], [1, 1, 1, 2, 1, 1, 1]),
    
    # Caso con una lista vacía
    ([], [1, 2, 3]),
    
    # Caso con ambas listas vacías
    ([], []),
    
    # Caso extremo: lista larga vs corta
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 6])
]

# Ejecutar casos de prueba
for a, b in casos_prueba:
    long, subsec = secuencias(a, b)
    print(f"\nProbando con:\na = {a}\nb = {b}")
    print(f"Longitud máxima: {long}")
    print(f"Subsecuencia común: {subsec}")

# TEST    

def test_secuencias():

    # Caso 1: estándar
    a1 = [0, 1, 1, 0, 1, 0, 1, 0]
    b1 = [1, 0, 1, 0, 0, 1, 0, 0, 1]
    long_esp1 = 6
    sec_esp1 = [0, 1, 1, 0, 0, 1]
    long1, subsec1 = secuencias(a1, b1)
    assert long_esp1 == long1
    assert sec_esp1 == subsec1

    # Caso 2: una única coincidencia
    a2 = [1, 2, 3]
    b2 = [4, 5, 1]
    long_esp2 = 1
    sec_esp2 = [1]
    long2, subsec2 = secuencias(a2, b2)
    assert long_esp2 == long2
    assert sec_esp2 == subsec2

    # Caso 3: sin subsecuencia común
    a3 = [0, 0, 0]
    b3 = [1, 1, 1]
    long_esp3 = 0
    sec_esp3 = []
    long3, subsec3 = secuencias(a3, b3)
    assert long_esp3 == long3
    assert sec_esp3 == subsec3

    # Caso 4: valores repetitivos
    a4 = [1, 1, 1, 1, 1, 2, 1]
    b4 = [1, 1, 1, 2, 1, 1, 1]
    long_esp4 = 6
    sec_esp4 = [1, 1, 1, 1, 1, 1]
    long4, subsec4 = secuencias(a4, b4)
    assert long_esp4 == long4
    assert sec_esp4 == subsec4

    # Caso 5: una lista vacía
    a5 = []
    b5 = [1, 2, 3]
    long_esp5 = 0
    sec_esp5 = []
    long5, subsec5 = secuencias(a5, b5)
    assert long_esp5 == long5
    assert sec_esp5 == subsec5

    # Caso 6: ambas listas vacías
    a6 = []
    b6 = []
    long_esp6 = 0
    sec_esp6 = []
    long6, subsec6 = secuencias(a6, b6)
    assert long_esp6 == long6
    assert sec_esp6 == subsec6

    # Caso 7, extremo: lista larga vs corta
    a7 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b7 = [5, 6]

    long_esp7 = 2
    sec_esp7 = [5, 6]

    long7, subsec7 = secuencias(a7, b7)
    assert long_esp7 == long7
    assert sec_esp7 == subsec7

# TEST DE RENDIMIENTO

# Test de rendimiento para un caso estándar
def test_secuencias_benchmark(benchmark):
    a = [0, 1, 1, 0, 1, 0, 1, 0]
    b = [1, 0, 1, 0, 0, 1, 0, 0, 1]

    def funcion_test_benchmark():
        long, subsec = secuencias(a, b)
        assert long == 6
        assert subsec == [0, 1, 1, 0, 0, 1]
        return long, subsec

    benchmark(funcion_test_benchmark)

# Test de rendimiento para un caso sin subsecuencia común
def test_secuencias_sin_coincidencias_benchmark(benchmark):
    a = [0, 0, 0]
    b = [1, 1, 1]

    def funcion_test_benchmark():
        long, subsec = secuencias(a, b)
        assert long == 0
        assert subsec == []
        return long, subsec

    benchmark(funcion_test_benchmark)

# Test de rendimiento para una lista vacía
def test_secuencias_lista_vacia_benchmark(benchmark):
    a = []
    b = [1, 2, 3]

    def funcion_test_benchmark():
        long, subsec = secuencias(a, b)
        assert long == 0
        assert subsec == []
        return long, subsec

    benchmark(funcion_test_benchmark)

# Test de rendimiento para un caso extremo (lista larga)
def test_secuencias_grande_benchmark(benchmark):
    a = list(range(1000))
    b = list(range(500, 1500))

    def funcion_test_benchmark():
        long, subsec = secuencias(a, b)
        assert long > 0  # Verifica que encuentra una subsecuencia
        return long, subsec

    benchmark(funcion_test_benchmark)