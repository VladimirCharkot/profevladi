belle = ['La belle verte', '1996', 'Comedy', '1h 39m']
mision = ['Misión imposible', '1996', 'Acción', '1h 23m']
huckabees = ['I heart Huckabees', 'Dark Comedy', '2004', '1h 47m']

pelis = [belle, mision, huckabees]

print('Consulta:')
nombre = input()

for peli in pelis:
    if peli[0] == nombre:
        print(peli[1])
