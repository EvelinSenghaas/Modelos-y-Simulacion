def fibonacci():
    try:
        print('Ingrese el parametro V1: ')
        v1 = Generador.isNegative(Generador.isNumber(input()))
        print('Ingrese el parametro V2: ')
        v2 = Generador.isNegative(Generador.isNumber(input()))
        print('Ingrese el parametro A: ')
        a = Generador.isNegative(Generador.isNumber(input()))
        print('Cuantos numeros quiere generar? : ')
        n = Generador.isNegative(Generador.isNumber(input()))
        print("Sucesion: ", Generador.fibonacci(v1, v2, a, n))
    except ValueError as e:
        print(e)


def congruencial_multiplicativo():
    pass


print(
    "Bienvenido, ingrese 1 para fibonacci o 2 para congruencial multiplicativo: "
)
# TODO: Validar la entrada
entrada = input()
if entrada == 1:
    fibonacci()
else:
    congruencial_multiplicativo()
