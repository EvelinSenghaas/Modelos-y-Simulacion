array= [2000,500,1000,1500,500,2000,2000,2000,2000,-500] #aca irian los valores
puertas = [0,0,0,0,0] #esto representara la cantidad de puertas que se abren en el año, por ejemplo puertas[0] = cant de veces que se abrio la puerta 1 en el año
caudal=45000 #tiene que ser dinamico
cambios = 0 #me va a representar la cantidad de puertas abiertas el dia anterior
escurrido=0 #va a representar el total de agua escurrida
perdida = 0 #perdida en megavtios total anual
for mc in array: #mc = valor del dia
    if cambios !=0:
        aux = cambios * 3000 #cambios va a ser 1,2,3 o 4 depende de las compuertas que se abrieron el dia anterior
        caudal -= aux 
        escurrido += aux 
        #367mv = 1tb -> 830ms ------------Una turbina genera 367megavatios con 830ms
        perdida += (aux/830) * 367 #me devuelve la cantidad de megavatios que perdi, para entender podes usar regla de 3 simple
        #ver algo de perdidas
        cambios = 0
    caudal += mc
    if caudal >= 15000:
        puertas[0] +=1 #esto servira para contar luego el total de puertas que se abrieron en el año
        cambios +=1
    if caudal >= 25000 :
        puertas[1] +=1
        cambios +=1
    if caudal >= 32000 :
        puertas[2] +=1
        cambios +=1
    if caudal >= 40000:
        puertas[3] +=1
        cambios +=1
    if caudal >= 45000:
        puertas[4] +=1 #puerta 4 es en realidad la alerta

print('# puerta 1 ', puertas[0])
print('# puerta 2 ', puertas[1])
print('# puerta 3 ', puertas[2])
print('# puerta 4 ', puertas[3])
print('# alertas ', puertas[4])
print('Total de agua escurrida ', escurrido)
print('perdida en megavatios ', perdida)

