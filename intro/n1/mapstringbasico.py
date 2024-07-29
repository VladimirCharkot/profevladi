frase = input('Ingresá una frase > ')

nueva = ''
for letra in frase:
    if letra in 'aeiou':
        nueva += 'i'
    else:
        nueva += letra

print(nueva)