import metodos
from utilidades import isNumber, isNegative, getSeed


def fibonacci():
    try:
        print('Ingrese el parametro V1: ')
        v1 = isNumber(isNegative(input()))
        print('Ingrese el parametro V2: ')
        v2 = isNumber(isNegative(input()))
        print('Ingrese el parametro A: ')
        a = isNumber(isNegative(input()))
        print('Cuantos numeros quiere generar? : ')
        n = isNumber(isNegative(input()))
        print("Sucesion: ", metodos.fibonacci(v1, v2, a, n))
    except ValueError as e:
        print(e)


def congruencialMultiplicativo():
    try:
        seed = getSeed()
        print('Ingrese el parametro A: ')
        a = isNumber(isNegative(input()))
        print('Cuantos numeros quiere generar? : ')
        n = isNumber(isNegative(input()))
        print("Sucesion: ", metodos.fibonacci(v1, a, n))
    except ValueError as e:
        print(e)


print(
    "Bienvenido, ingrese 1 para fibonacci o 2 para congruencial multiplicativo: "
)
# TODO: Validar la entrada
entrada = input()
if entrada == 1:
    fibonacci()
else:
    congruencial_multiplicativo()
