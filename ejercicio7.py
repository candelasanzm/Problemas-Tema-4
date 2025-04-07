def secuencias(a,b):
    n = len(a)
    m = len(b)
    matriz = []
    #construir la matriz
    for i in range(n+1):
        fila=[]
        for j in range(m+1):
            fila.append(0)
        matriz.append(fila)
    #llenar la matriz
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i-1] == b[j-1]:
                matriz[i][j] = matriz[i-1][j-1] + 1
            else:
                matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1])
    #subsecuencia común
    i = n
    j = m
    subsec = []
    while i>0 and j>0:
        if a[i-1] == b[j-1]:
            subsec.append(a[i-1])
            i-=1
            j-=1
        elif matriz[i-1][j] >= matriz[i][j-1]:
            i-=1
        else:
            j-=1
    subsec.reverse()
    return matriz[n][m], subsec

a = [0,1,1,0,1,0,1,0]
b = [1,0,1,0,0,1,0,0,1]


long, subsecuencia = secuencias(a,b)
print("Longitud maxima: ", long)
print("Subsecuencia común", subsecuencia)

def test_secuencias():
    #Prueba 1: secuencias cortas 
    a1 = [1,0,1,1]
    b1 = [0,1,1,0]

    long_esp1 = 3
    sec_esp1 = [0,1,1]

    long1, subsec1 = secuencias(a1,b1)
    assert long_esp1 == long1
    assert sec_esp1 == subsec1

    #Prueba 2: secuencias largas
    a2 = [0,1,1,0,1,0,1,0]
    b2 = [1,0,1,0,0,1,0,0,1]

    long_esp2 = 6
    sec_esp2 = [0,1,1,0,0,1]

    long2, subsec2 = secuencias(a2,b2)
    assert long_esp2 == long2
    assert sec_esp2 == subsec2
    
    #Prueba 3: no hay subsecuencias en común
    a3 = [0,0,0]
    b3 = [1,1,1]

    long_esp3 = 0
    sec_esp3 = []

    long3, subsec3 = secuencias(a3,b3)
    assert long_esp3 == long3
    assert sec_esp3 == subsec3

    #Prueba 4: coinciden 
    a4 = [1,0,1,1]
    b4 = [1,0,1,1]

    long_esp4 = 4
    sec_esp4 = [1,0,1,1]

    long4, subsec4 = secuencias(a4,b4)
    assert long_esp4 == long4
    assert sec_esp4 == subsec4