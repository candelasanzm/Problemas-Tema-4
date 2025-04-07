"""
Ejercicio 1. Programación Dinámica
=================================
    - Coste menor de un camino en una matriz.
    - Se puede mover a la derecha o hacia abajo.
    - El coste de un camino es la suma de los valores de las celdas que lo
      componen.

    Ejemplo:
        3 2 3 2 5
        1 2 4 5 6
        4 3 6 2 4
        2 5 3 4 3

    Coste menor: 24 (3 + 2 + 4 + 5 + 6 + 4)
"""

def mejor_camino(matriz):
    # Inicialización
    n = len(matriz)
    m = len(matriz[0])
    matriz_coste = [[0] * m for _ in range(n)]
    matriz_caminos = [[[] for _ in range(m)] for _ in range(n)]

    matriz_coste[0][0] = matriz[0][0]

    # Algoritmo
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if i == 0:
                matriz_coste[i][j] = matriz_coste[i][j-1] + matriz[i][j]
                matriz_caminos[i][j] = matriz_caminos[i][j-1] + ['derecha']
            elif j == 0:
                matriz_coste[i][j] = matriz_coste[i-1][j] + matriz[i][j]
                matriz_caminos[i][j] = matriz_caminos[i-1][j] + ['abajo']
            else:
                if matriz_coste[i-1][j] < matriz_coste[i][j-1]:
                    matriz_coste[i][j] = matriz_coste[i-1][j] + matriz[i][j]
                    matriz_caminos[i][j] = matriz_caminos[i-1][j] + ['abajo']
                else:
                    matriz_coste[i][j] = matriz_coste[i][j-1] + matriz[i][j]
                    matriz_caminos[i][j] = matriz_caminos[i][j-1] + ['derecha']

    return matriz_coste[-1][-1], matriz_caminos[-1][-1]


matriz = [ [3, 2, 3, 2, 5],
           [1, 2, 4, 5, 6],
           [4, 3, 6, 2, 4],
           [2, 5, 3, 4, 3] ]

camino = mejor_camino(matriz)
print(f"El menor coste y el mejor camino son: {camino}")  # Salida: 24
