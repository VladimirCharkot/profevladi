frase = input('Ingresá una frase')

# Clase 4 - Hola for

nueva = ''
for letra in frase:
    if letra in 'aeiou':
        nueva += 'i'
    else:
        nueva += letra
