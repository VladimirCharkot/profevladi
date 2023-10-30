belle = {'genero' : 'Comedy', 'nombre' : 'La belle verte', 'año' : '1996', 'duracion' : '1h 39m'}
mision = {'nombre' : 'Misión imposible', 'genero' : 'Acción', 'duracion' : '1h 23m', 'año' : '1996'}
mision2 = {'nombre' : 'Misión imposible 2', 'genero' : 'Acción', 'duracion' : '1h 23m', 'año' : '1998'}
huckabees = {'año' : '2004', 'genero' : 'Dark Comedy', 'nombre' : 'I heart Huckabees', 'duracion' : '1h 47m'}

pelis = [belle, mision, huckabees, mision2]

print('Ingresá nombre:')
nombre = input()

tengo = False
for peli in pelis:
    if nombre == peli['nombre']:
        tengo = True

if tengo:
    print('Ingresá dato que querés:')
    dato = input()

    for peli in pelis:
        if peli['nombre'] == nombre:
            if dato in peli:
                print(peli[dato])
            else:
                print('No tengo ese dato para esta peli')

else:
    print('No lo tengo')

print('Gracias vuelva prontos')
