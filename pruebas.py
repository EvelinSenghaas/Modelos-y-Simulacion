from monobitsTest import convertSerieToOneZero, convertSerieToOneOne, sumatoriaXi, Sobs, P_value
# serie = ["19", "53", "72", "22", "94", "13", "4", "17", "21", "38"]
serie = [
    "19", "103", "122", "225", "120", "118", "11", "129", "140", "42", "182",
    "224"
]
length = len(serie)

print("####  TEST DE MONOBITS  ####")
print("La serie a testear es: " + str(serie))
print("")
print("")
serie = convertSerieToOneZero(serie)
print("La serie convertida en 0 y 1: " + str(serie))
print("")
print("")
serie = convertSerieToOneOne(serie)
print("La serie convertida en -1 y 1 : " + str(serie))
print("")
print("")
sumatoria = sumatoriaXi(serie)
print("La sumatoria de la serie es: " + str(sumatoria))
print("")
print("")
sobs = Sobs(sumatoria, length)
print("La prueba estadistica es: " + str(sobs))
print("")
print("")
p = P_value(sobs)
print("El P-valor es: " + str(p))
print("")
print("")
if p > 0.001:
    print("Paso la prueba")
else:
    print("NO paso la prueba")