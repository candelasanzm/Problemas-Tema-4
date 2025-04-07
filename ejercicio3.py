"""
v son los valores de los billetes ordenador de menor a mayor
c es la cantidad de billetes de cada valor, debe ser una lista de la misma longitud que v
D cantida de dinero que se quiere pagar
"""
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

# Ejemplo de uso
billetes = [
    billetes_dict(1, 10),
    billetes_dict(2, 5),
    billetes_dict(5, 2),
    billetes_dict(10, 2),
    billetes_dict(20, 1),
]

D = 27
res = devolver_cantidad_exacta(billetes, D)
print(res)

def test_devolver_cantidad_exacta():
    