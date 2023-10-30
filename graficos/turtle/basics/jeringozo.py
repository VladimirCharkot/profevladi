texto = input('Ingresate un texto: ')

# Convertir en función?:
nuevo = ''

for letra in texto:
    if letra in 'aeiou':
        nuevo += letra + 'p' + letra
    else:
        nuevo += letra

print(nuevo)


