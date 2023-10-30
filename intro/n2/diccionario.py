f = open('castellano.txt', encoding='utf8')
lineas = f.readlines()
f.close()

# Python 2 - Paradigmas


##palabras = []
##for linea in lineas:
##    palabras.append(linea.replace('\n',''))

palabras = [linea.replace('\n','') for linea in lineas]

def no_contiene(letras, palabra):
    return all([not letra in palabra for letra in letras])

def solo_a(palabra):
    return no_contiene('eiouéíóú', palabra)

def solo_e(palabra):
    return no_contiene('aiouáíóú', palabra)

def solo_i(palabra):
    return no_contiene('aeouáéóú', palabra)

def solo_o(palabra):
    return no_contiene('aeiuáéíú', palabra)

def solo_u(palabra):
    return no_contiene('aeioáéíó', palabra)

aes = [p for p in palabras if solo_a(p)]
ees = [silla for silla in palabras if solo_e(silla)]
ies = [p for p in palabras if solo_i(p)]
oes = [p for p in palabras if solo_o(p)]
ues = [p for p in palabras if solo_u(p)]

##aes = []
##for palabra in palabras:
##    if not 'e' in palabra \
##    and not 'i' in palabra\
##    and not 'o' in palabra\
##    and not 'u' in palabra\
##    and not 'é' in palabra\
##    and not 'í' in palabra\
##    and not 'ó' in palabra\
##    and not 'ú' in palabra:
##        aes.append(palabra)

#Filtro
largas = [p for p in palabras if len(p) > 15]

##largas = []
##for palabra in palabras:
##    if len(palabra) > 15:
##        largas.append(palabra)

# Mapeo
torcidas = [p[-1] + p[1:-1] + p[0] for p in palabras]

##torcidas = []
##for palabra in palabras:
##    torcidas.append(palabra[-1] + palabra[1:-1] + palabra[0])



# Ejercicio 3

# Filtros:
# Palabras que terminen con ina     p.endswith('ina')
inas = [p for p in palabras if p.endswith('ina')]
# Palabras que terminen con ón
# Palabras que empiecen y terminen con la misma letra

# Mapeos:
# Palabras pero sin las vocales
# Palabras pero con dos letras al azar intercambiadas
# Palabras invertidas               p[::-1]
invertidas = [p[::-1] for p in palabras]

# Extra:
# Producir una lista de palabras cuyas inversas se encuentren en el diccionario
