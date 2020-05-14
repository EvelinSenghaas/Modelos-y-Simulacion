from utilidades import validateChiCuadrado


def chiCuadrado(serie, k):
    #serie es un array que lo generan los otros metodos
    fi = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cadena = ''
    for num in serie:
        cadena += str(num)
    for n in cadena:
        fi[int(n)] += 1
    n = len(cadena)
    if k > 9:
        k = 10
    gl = k - 1  #grados de libertad siempre en 9 porque usamos 10 digitos
    npi = n / k
    frecuencia = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    i = 0
    chi = 0
    for f in fi:
        #f = una de las frecuencias reales (osea lo que obtuvimos en la muestra)
        #voy a restar esa frecuencia real menos la esperada es decir f - npi y luego elevo al cuadraro
        #y luego divido por la frecuencia esperada
        frecuencia[i] = ((f - npi)**2) / npi
        chi += frecuencia[i]
        i += 1
    if validateChiCuadrado(chi, gl):
        print('paso la prueba!!!')
    else:
        print('suerte la proxima')
    print('frecuencia ', frecuencia)
    return validateChiCuadrado(chi, gl)
