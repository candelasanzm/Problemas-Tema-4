"""
v son los valores de los billetes ordenador de menor a mayor
c es la cantidad de billetes de cada valor, debe ser una lista de la misma longitud que v
D cantida de dinero que se quiere pagar
"""

# FUNCIONES

def billetes_dict(v : int, c : int) -> dict:
    """ Diccionario para almacenar los datos de un billete (cuanto vale y la cantidad de estos que hay) """
    return {'valor' : v, 'cantidad' : c}

def devolver_cantidad_exacta(b : list[dict], D : int) -> tuple[bool, list[int]]:
    """ Determinar si se puede devolver la cantidad de forma exacta y calcular su descomposición """
    
    numeroBilletes = len(b)

    # Representamos la tabla dinámica dp[i][j], donde j es la cantidad que queremos alcanzar e i los tipos de billetes
    matriz = [[float('inf')] * (D + 1) for _ in range (numeroBilletes + 1)]

    # Caso base: si hay que devolver 0 euros no se necesitan billetes
    matriz[0][0] = 0

    # Construcción de la tabla dinámica
    for i in range(1, numeroBilletes + 1): # itero sobre los tipos de billetes
        for j in range(D + 1): # itero sobre las cantidades de los billetes
            matriz[i][j] = matriz[i - 1][j]

            for k in range(b[i - 1]['cantidad'] + 1): # itero sobre la cantidad de billetes disponibles de un tipo concreto
                if k * b[i - 1]['valor'] <= j:
                    matriz[i][j] = min(matriz[i][j], matriz[i - 1][j - k * b[i - 1]['valor']] + k)

    # Hay que ver si es posible devolver la cantidad D o no
    if matriz[numeroBilletes][D] == float('inf'):
        return False, []
    
    # Construimos el resultado 
    resultado = [0] * numeroBilletes # Lista donde vamos a almacenar cuántos billetes de cada tipo
    s = D # comenzamos en la cantidad total
    for i in range(numeroBilletes, 0, -1):
        for k in range(b[i - 1]['cantidad'] + 1):
            if s >= k * b[i - 1]['valor'] and matriz[i][s] == matriz[i - 1][s - k * b[i - 1]['valor']] + k:
                resultado[i - 1] = k
                s -= k * b[i - 1]['valor']
                break

    return True, resultado

# CASOS DE PRUEBA

casos_prueba = [
    # Casos estándar
    ([billetes_dict(1, 10), billetes_dict(2, 5), billetes_dict(5, 2), billetes_dict(10, 2), billetes_dict(20, 1)], 27),
    ([billetes_dict(1, 5), billetes_dict(2, 3), billetes_dict(5, 4)], 8),
    
    # Casos extremos
    ([billetes_dict(1, 100)], 99),
    ([billetes_dict(50, 2), billetes_dict(20, 1)], 90),
    
    # Casos con billetes insuficientes
    ([billetes_dict(3, 4), billetes_dict(7, 2)], 5),
    
    # Casos con billetes desordenados
    ([billetes_dict(10, 2), billetes_dict(1, 10), billetes_dict(20, 1), billetes_dict(5, 2)], 27),
    
    # Casos límite
    ([billetes_dict(10, 1)], 10),
    ([billetes_dict(1, 1)], 1),
    ([billetes_dict(5, 3)], 0),
    
    # Caso imposible
    ([billetes_dict(50, 3), billetes_dict(100, 2)], 30),
]

# Ejecución de los casos de prueba
for billetes, D in casos_prueba:
    print(f"\nProbando con cantidad: {D} y billetes: {billetes}")
    resultado = devolver_cantidad_exacta(billetes, D)
    print(f"Resultado: {resultado}")

# TEST

def test_devolver_cantidad_exacta():
    billetes = [
        billetes_dict(1, 10),
        billetes_dict(2, 5),
        billetes_dict(5, 2),
        billetes_dict(10, 2),
        billetes_dict(20, 1),
    ]

    # Caso donde se puede devolver la cantidad exacta
    D1 = 27
    resultado1 = (True, [0, 1, 1, 0, 1])
    assert devolver_cantidad_exacta(billetes, D1) == resultado1

    # Caso donde no se puede devolver la cantidad exacta, sin solución
    D2 = 90
    resultado2 = (False, [])
    assert devolver_cantidad_exacta(billetes, D2) == resultado2

    # Caso con una cantidad exacta y un único tipo de billetes
    billetes2 = [billetes_dict(10, 3)]
    D3 = 20
    resultado3 = (True, [2])
    assert devolver_cantidad_exacta(billetes2, D3) == resultado3

    # Caso con D = 0
    D4 = 0
    resultado4 = (True, [0, 0, 0, 0, 0])
    assert devolver_cantidad_exacta(billetes, D4) == resultado4

    # Caso con D = 1
    D5 = 1
    resultado5 = (True, [1, 0, 0, 0, 0])
    assert devolver_cantidad_exacta(billetes, D5) == resultado5

    # Caso con billetes insuficientes
    billetes3 = [billetes_dict(3, 4), billetes_dict(7, 2)]
    D6 = 5
    resultado6 = (False, [])
    assert devolver_cantidad_exacta(billetes3, D6) == resultado6

    # Caso con valores de billetes desordenados
    billetes4 = [billetes_dict(10, 2), billetes_dict(1, 10), billetes_dict(20, 1), billetes_dict(5, 2)]
    D7 = 27
    resultado7 = (True, [0, 2, 1, 1])
    assert devolver_cantidad_exacta(billetes4, D7) == resultado7

    # Caso con billetes que sobrepasan D
    billetes5 = [billetes_dict(50, 3), billetes_dict(100, 2)]
    D8 = 30
    resultado8 = (False, [])
    assert devolver_cantidad_exacta(billetes5, D8) == resultado8

    # Caso con billetes de valor 1
    billetes6 = [billetes_dict(1, 100)]
    D9 = 15
    resultado9 = (True, [15])
    assert devolver_cantidad_exacta(billetes6, D9) == resultado9