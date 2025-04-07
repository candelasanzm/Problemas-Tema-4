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