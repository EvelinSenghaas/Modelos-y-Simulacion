""" MARCAS DE CLASES """


# Define los minimos y maximos para cada marca de clase
def setMinAndMax(classMarks, min, max):
    quantitySymbols = max - min
    for classMark in classMarks:
        classMark['minimum'] = min
        if min == 0:
            classMark['maximum'] = min + (quantitySymbols * float(classMark['expectedProbability']))
        else:
            classMark['maximum'] = min + (quantitySymbols * 
                float(classMark['expectedProbability'])) - 0.0001
        min = classMark['maximum'] + 0.0001
    return classMarks


# Recorre la serie y sumando las apariciones de number dentro de cada marca de clase
def setAppearances(serie, classMarks):
    for number in serie:
        number = float(number)
        for classMark in classMarks:
            if number >= classMark['minimum'] and number <= classMark['maximum']:
                classMark['appearances'] += 1
                break
    return classMarks


# Determina la probabilidad obtenide en base a las apariciones de cada clase y el total de la serie
def setObtainedProbability(classMarks, total):
    for classMark in classMarks:
        classMark['obtainedProbability'] = classMark['appearances'] / float(total)
    return classMarks


def setAttributes(classMarks):
    for classMark in classMarks:
        classMark['appearances'] = 0
        classMark['obtainedProbability'] = 0
        classMark['minimum'] = 0
        classMark['maximum'] = 0
    return classMarks


# Metodo de marcas de clase
def runClassMarks(classMarks, serie, min, max):
    classMarks = setAttributes(classMarks)
    classMarks = setMinAndMax(classMarks, min, max)
    classMarks = setAppearances(serie, classMarks)
    classMarks = setObtainedProbability(classMarks, len(serie))
    return classMarks
