""" MONO BITS TEST """
from math import sqrt, pi, exp
import scipy.integrate as integrate
from scipy.special import np


# Convertir la serie en 0 o 1
def convertSerieToOneZero(serie):
    serie = ''.join(serie)
    result = []
    for i in range(0, len(serie)):
        if int(serie[i]) >= 5:
            result.append(1)
        else:
            result.append(0)
    return result


# Convertir la serie en -1 o 1
def convertSerieToOneOne(serie):
    result = []
    for i in range(0, len(serie)):
        result.append(2 * serie[i] - 1)
    return result


# Sumatoria de la -1 y 1 de la serie
def sumatoriaXi(serie):
    S = 0
    for s in serie:
        S += s
    return S


# Calcula la prueba estadistica
def Sobs(Sn, n):
    return abs(Sn) / sqrt(n)


# Calcula el P-valor
def P_value(Sobs):
    z = Sobs / sqrt(2)  #erfc
    a = 2 / sqrt(pi)
    return a * integrate.quad(lambda x: exp(-x**2), z, np.inf)[0]


# Realiza el test de monobits sobre una serie
def test(serie):
    length = len(serie)
    result = P_value(
        Sobs(sumatoriaXi(convertSerieToOneOne(convertSerieToOneZero(serie))),
             length))
    print(result)
    if result > 0.01:
        return True
    return False