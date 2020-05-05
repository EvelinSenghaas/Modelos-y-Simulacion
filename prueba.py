
def numero(cero): #Esta funcion utilizo para validar las entradas
    aux = True
    while aux:
        try:
            v= int(input()) #v es el valor ingresado, lo que voy a retornar 
            if cero: #osea si cero es true es porque v puede valer cero
                aux = False
            else:
                if v==0:
                    print('ingrese un valor mayor a cero')
                else:
                    aux=False
        except:
            print('Ingrese valores enteros por favor')
    return v

def fibonacci(v1,v2,a,n):
    i=0
    sucesion = str(v1) + str(v2)
    while(i < n):
        if v2 + v1 <= a:
            k=0
        else:
            k=-1
        v3 = v1+v2+k*a
        sucesion += str(v3)
        v1 = v2
        v2 = v3
        i+=1
    return sucesion

def congruencial(s,n,a,m): #bueno este metodo generara numeros aleatorios entre cero y nueve
    resultado = []
    resultado.append(str(s))
    secuencia = str(s)
    i=0
    while i < n:
        v = (a * int(resultado[i])) %m
        resultado.append(str(v))
        secuencia=str(v)
        i+=1
    return secuencia

def is_prime(num): 
    if num < 1:
        return False
    elif num == 2:
        return True
        print('primoncho')
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        print('primonncho')
        return True   
#METODO FIOBANACCI
'''print('ingresa el v1')
cero=True #esta variable cero me va a servir para que no ingresen todo cero
#cero = True es que admite cero
v1 = numero(cero)
print('ingresa el valor v2')
if v1 == 0:
    cero = False #v2 no va a poder ser cero
v2= numero(cero)
print('ingresa el valor a')
cero = False
a= numero(cero) #a nunca deberia valer 0
print('ingresa el valor de n')
n= numero(cero) #n tampoco deberia ser cero
print('metodo fiobanacci',fibonacci(v1,v2,a,n))'''

#METODO CONGRUENCIAL ADITIVO 
semilla = int(input('semilla:'))
while (semilla%2 ==0 or semilla%5==0):
    semilla = int(input('semilla:'))
    if is_prime(semilla):
        break #osea si es primo ya es primo con respecto a la m
    #hay que ver si no
a = 13
print('Inserte la cantidad de numeros a generar') #No se como decirlo mejor, osea no es que si vos poner quiero 3 numeros vas a tener 3... no si no que va haber 3 repeticiones
n=numero(False) #distinto de cero claro
m= 32 #2^d
print('metodo congruencial multiplicativo', congruencial(semilla,n,a,m))
# n = cant numeros a generar



    