n = 0

texto = input('Ingresá una frase > ')
texto_nuevo = ''

while n < len(texto):
    letra = texto[n]
    if letra in 'aeiou':
        texto_nuevo = texto_nuevo + 'i'
    else:
        texto_nuevo = texto_nuevo + letra
    n = n + 1

print(texto_nuevo)
