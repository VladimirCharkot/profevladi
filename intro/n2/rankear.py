def limpiar(palabra):
    palabra = palabra.replace('.', '')
    palabra = palabra.replace(',', '')
    palabra = palabra.replace(':', '')
    palabra = palabra.replace(';', '')
    palabra = palabra.replace('!', '')
    palabra = palabra.replace('?', '')
    palabra = palabra.replace('¡', '')
    palabra = palabra.replace('¿', '')
    palabra = palabra.replace('-', '')
    palabra = palabra.replace('"', '')
    palabra = palabra.replace('(', '')
    palabra = palabra.replace(')', '')
    palabra = palabra.lower()
    return palabra

def palabras(contenido_texto):
    texto = contenido_texto.replace('\n', ' ')
    principito_palabras = texto.split()

    palabras_limpias = []
    for palabra in principito_palabras:
        palabras_limpias.append(limpiar(palabra))

    pals = set(palabras_limpias)

    cuenta = []
    for pal in pals:
        n = palabras_limpias.count(pal)
        par = [n, pal]
        cuenta.append(par)

    cuenta.sort()
    cuenta.reverse()


    for par in cuenta[:50]:
        print(str(par[0]) + ' | ' + par[1])
