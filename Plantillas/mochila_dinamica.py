"""
MOCHILA DINÁMICA (cada 0.5L)
Tenemos objetos de distintos valores y volúmenes, y queremos llenar una mochila
maximizando el valor de su contenido.

Mochila:
- Capacidad de 4L.
Objetos:
- Tablet (100€ / 1L)
- Ordenador (200€ / 2L)
- Móvil (80€ / 0.5L)
- Cargador (40€ / 1.5L)
"""

def _objeto(nombre :str, valor :float, volumen :float) -> dict:
    """ Diccionario para almacenar los datos de un objeto """
    return {'nombre': nombre, 'valor': valor, 'volumen': volumen}

def mochila_dinamica(objetos: list[_objeto], capacidad: int):
    # Inicialización
    n = len(objetos)
    capacidades = []
    for i in range(capacidad * 2 + 1):
        capacidades += [i / 2]
    matriz = []
    for f in range(n + 1):
        matriz += [[]]
        for c in range(len(capacidades)):
            matriz[f] += [0]
    # Algoritmo
    for i in range(1, n + 1):
        for j in range(1, len(capacidades)):
            if objetos[i-1]['volumen'] <= capacidades[j]:
                anterior = capacidades[j] - objetos[i-1]['volumen']
                col = 0
                while capacidades[col] < anterior:
                    col += 1
                nuevo = objetos[i-1]['valor'] + matriz[i-1][col]
                matriz[i][j] = max(nuevo, matriz[i-1][j])
            else:
                matriz[i][j] = matriz[i-1][j]

    return matriz[n][-1]

# Ejemplo de uso
objetos = [ _objeto('Tablet',    100, 1),
            _objeto('Ordenador', 200, 2),
            _objeto('Móvil',     80,  0.5),
            _objeto('Cargador',  40,  1.5) ]

capacidad = 4
print(mochila_dinamica(objetos, capacidad))  # Salida: 380
