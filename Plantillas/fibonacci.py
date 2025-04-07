def fibonacci(n :int) -> int:
    """ n-ésimo término de la sucesión de fibonacci """
    assert n >= 0, "n debe ser mayor o igual a 0"
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_cache(n :int) -> int:
    """ n-ésimo término de la sucesión de fibonacci """
    assert n >= 0, "n debe ser mayor o igual a 0"
    
    def _fibonacci_cache(n: int, cache: dict) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        else:
            resultado = _fibonacci_cache(n - 1, cache) + _fibonacci_cache(n - 2, cache)
            cache[n] = resultado
            if len(cache) > 2:
                del cache[n - 2]
            return resultado
        
    cache = {}
    return _fibonacci_cache(n, cache)

def fibonacci_dinamico(n: int) -> int:
    cache = [0, 1]
    for i in range(2, n + 1):
        cache.append(cache[i - 1] + cache[i - 2])
    return cache[n]

def fibonacci_dinamico2(n: int) -> int:
    cache = [0, 1]
    for _ in range(2, n + 1):
        aux = cache[0]
        cache[0] = cache[1]
        cache[1] += aux
    return cache[1]

# Probador
print(fibonacci(30))
print(fibonacci_cache(30))
print(fibonacci_dinamico(30))
print(fibonacci_dinamico2(30))
