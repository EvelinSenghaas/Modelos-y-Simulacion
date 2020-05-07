""" METODOS """
import utilidades
from utilidades import isPrime


# genera una sucesion de numeros pseudoaleatorios con el metodo fibonacci
def fibonacci(v1, v2, a, n):
    i = 0
    sucesion = [v1, v2]
    while (i < n):
        if v2 + v1 <= a:
            k = 0
        else:
            k = -1
        v3 = v1 + v2 + k*a
        sucesion.append(str(v3))
        v1 = v2
        v2 = v3
        i += 1
    return sucesion


#bueno este metodo generara numeros aleatorios entre cero y nueve
def congruencialMultiplicativo(s, n, a, m):
    resultado = []
    resultado.append(str(s))
    i = 0
    while i < n:
        v = (a * int(resultado[i])) % m
        resultado.append(str(v))
        i += 1
    return resultado