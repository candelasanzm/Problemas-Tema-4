def binomial(n: int, k: int) -> int:
    if k == 0:
        return 1
    if n == k:
        return 1
    return binomial(n-1, k-1) + binomial(n-1, k)

def binomial_dinamico(n: int, k: int) -> int:
    
    def _matriz_binomial(n: int, k: int) -> list[list[int]]:
        """
            _matriz_binomial(n, k) es la matriz de orden (n+1)x(k+1) tal que el valor en
            la posición (i,j) (con j <= i) es el coeficiente binomial i sobre j. 
            Por ejemplo:
              _matriz_binomial(3, 3) = [[1, 0, 0, 0], 
                                        [1, 1, 0, 0], 
                                        [1, 2, 1, 0], 
                                        [1, 3, 3, 1]]
        """
        matriz = [[0 for i in range(k + 1)] for j in range(n + 1)]
        for i in range(n + 1):
            for j in range(min(i, k) + 1):
                if j == 0:
                    matriz[i][j] = 1
                elif i == j:
                    matriz[i][j] = 1
                else:
                    matriz[i][j] = matriz[i - 1][j - 1] + matriz[i - 1][j]
        return matriz
    
    return _matriz_binomial(n, k)[n][k]

# Probador
print(binomial(8, 3))
print(binomial_dinamico(8, 3))