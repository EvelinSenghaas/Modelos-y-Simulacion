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


# Verifica si ambas semillas son 0, e informa el mayor
def areZero(v1, v2):
    if v1 == 0 and v2 == 0:
        return True
    if v1 > v2:
        print("A debe ser mayor que ", v1)
    else:
        print("A debe ser mayor que ", v2)
    return False


# Verifica la divisibilidad entre 2 numeros con respecto a la semilla
def checkDivisibility(a=2, b=5):
    seed = int(input('semilla:'))
    while (seed % 2 == 0 or seed % 5 == 0):
        print("Error: semilla divisible por 2 o 5. \n")
        seed = int(input('Semilla:'))