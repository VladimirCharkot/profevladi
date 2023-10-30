# Diccionario literal: 
ab = {'nombre' : 'Abril', 'apellido' : 'Spremic', 'edad' : 27}

print(type(ab))

# Asignando nuevas clave/valor
ab['signo'] = 'géminis'
ab['amigues'] = ['Aleja', 'Fere', 'Vladi', 'Lucas']

# Al iterar un diccionario, se iteran sus CLAVES
for k in ab:
    print(k)

# Usamos esas claves para acceder a los valores:
for k in ab:
    print(k, ab[k])

al = {
    'nombre': 'Aleja',
    'apellido': 'Correa',
    'edad' : 30,
    'signo' : 'piscis',
    'amigues' : ['Abril', 'Vladi', 'Fere', 'Sofi', 'Pau']
}

fe = {
    'nombre': 'Fere',
    'apellido': 'Alarcón',
    'edad' : 27,
    'signo' : 'acuario',
    'amigues' : ['Abril', 'Vladi', 'Aleja', 'Manu', 'Lin']
}

vl = {
    'nombre': 'Vladi',
    'apellido': 'Charkot',
    'edad' : 29,
    'signo' : 'géminis',
    'amigues' : ['Abril', 'Aleja', 'Fere', 'Diego', 'Maxi', 'Rodri']
}


banda = [ab, al, fe, vl]


# Podemos usar el operador in, tanto con listas como con diccionarios
# Con listas pregunta si el operando es un elemento de la lista
# Con diccionarios, pregunta si es una CLAVE


# Sets: nuestros queridos conjuntos, con intersecciones, uniones, y toda la bola

amis_vl = set(vl['amigues'])
amis_ale = set(al['amigues'])

# Intersección:
print(amis_vl & amis_ale)

# Unión:
print(amis_vl | amis_ale)

# Diferencia:
print(amis_vl - amis_ale)
print(amis_ale - amis_vl)


# Escribir una función que reciba un nombre
# y printeé las edades y signos de lxs amigues 
# de ese nombre que estén disponibles (que estén en la lista "banda")

# e.g.:
# asoc('Vladi')
# > 27 géminis
# > 30 piscis
# > 27 acuario


# Sets:
# Escribir una función que reciba dos nombres y printeé
# la diferencia simétrica entre los sets de amigues de ambxs
