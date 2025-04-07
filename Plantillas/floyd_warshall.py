def floyd_warshall(grafo):
    """ Algoritmo de Floyd-Warshall """
    
    # Diccionario para almacenar los nodos y sus posiciones
    nodos = {}
    pos = 0
    for v in grafo:
        nodos[v] = pos
        pos += 1

    # Inicialización de la matriz de distancias y caminos
    distancias = []
    caminos = []
    for _ in nodos:
        distancias.append([float('inf')] * len(nodos))
        caminos.append([None] * len(nodos))
    for origen in grafo:
        i = nodos[origen]
        distancias[i][i] = 0
        caminos[i][i] = origen
        for destino, peso in grafo[origen].items():
            j = nodos[destino]
            distancias[i][j] = peso
            caminos[i][j] = origen

    # Algoritmo
    n = len(nodos)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancias[i][k] + distancias[k][j] < distancias[i][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
                    caminos[i][j] = caminos[k][j]

    return nodos, distancias, caminos
    

# Programa
grafo = { # origen: {destino: peso}
    'a': {'b': 4, 'c': 3},
    'b': {'d': 5},
    'c': {'b': 2, 'd': 3, 'e': 6},
    'd': {'f': 5, 'e': 1},
    'e': {'g': 5},
    'g': {'z': 4},
    'f': {'g': 2, 'z': 7},
    'z': {}
}

nodos, distancias, caminos = floyd_warshall(grafo)
print(f'Nodos: {nodos}')
print('Distancias:')
print('------------------------------------------------')
for fila in distancias:
    for elem in fila:
        print(f'{elem:5}', end='')
    print()
print('------------------------------------------------')
print('Caminos:')
print('------------------------------------------------')
for fila in caminos:
    for elem in fila:
        if elem:
            print(f'{elem:5}', end='')
        else:
            print('no   ', end='')
    print()
print('------------------------------------------------')
