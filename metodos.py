""" METODOS """
import utilidades
from utilidades import isPrime

# genera una sucesion de numeros pseudoaleatorios con el metodo fibonacci
def fibonacci(v1, v2, a, n):
    i = 0
    sucesion = str(v1) + str(v2)
    while (i < n):
        if v2 + v1 <= a:
            k = 0
        else:
            k = -1
        v3 = v1 + v2 + k * a
        sucesion += str(v3)
        v1 = v2
        v2 = v3
        i += 1
    return sucesion


#bueno este metodo generara numeros aleatorios entre cero y nueve
def congruencial_multiplicativo(s, n, a, m):
    resultado = []
    resultado.append(str(s))
    secuencia = str(s)
    i = 0
    while i < n:
        v = (a * int(resultado[i])) % m
        resultado.append(str(v))
        secuencia = str(v)
        i += 1
    return secuencia


def congruencial_multiplicativo():
    semilla = int(input('semilla:'))
    while (semilla % 2 == 0 or semilla % 5 == 0):
        semilla = int(input('semilla:'))
        if isPrime(semilla):
            break  #osea si es primo ya es primo con respecto a la m
        #hay que ver si no