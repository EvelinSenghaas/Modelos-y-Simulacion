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