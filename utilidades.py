""" UTILIDADES """


# valida si el numero es positivo
def isNegative(number):
    if number < 0:
        raise ValueError("El parametro debe ser positivo.")
    return number


# valida si es un numero entero
def isNumber(param):
    if type(param) != int:
        raise ValueError("El parametro debe ser un numero.")
    return param


# Valida si el parametro es de 3 a 7
def between3_7(param):
    number_digits = len(str(param))
    if number_digits not in range(3, 8):
        raise ValueError("El parametro debe tener de 3 a 7 digitos.")
    return param


# Verifica si el numero es primo
def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


# Verifica si ambas semillas son 0, y retorna el mayor el mayor
def validateSeeds(v1, v2):
    if v1 == 0 and v2 == 0:
        raise ValueError("Error: ambas semillas son igual a 0")
    if v1 >= v2:
        return v1
    return v2


# Obtiene una semilla valida para el generador
def getSeed():
    print("Ingrese una semilla: ")
    seed = isNumber(isNegative(int(input())))
    while (seed % 2 == 0 or seed % 5 == 0):
        print("Error: semilla divisible por 2 o 5. \n")
        seed = int(input('Semilla:'))
    return seed


def validateChiCuadrado(chi, gl):
    dic = {
        1: 2.7055,
        2: 4.6052,
        4: 7.7794,
        6: 10.446,
        9: 14.6837,
    }
    valor = dic[gl]
    if chi < valor:
        return True
    else:
        return False