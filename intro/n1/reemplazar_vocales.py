n = 0

texto = 'Hola como tas'
texto_nuevo = ''

while n < len(texto):
    letra = texto[n]
    if letra in 'aeiou':
        texto_nuevo = texto_nuevo + 'a'
    else:
        texto_nuevo = texto_nuevo + letra
    n = n + 1

print(texto_nuevo)
