# Además de las funciones, que reciben y devuelven datos,
# existen los *métodos*, funciones anexadas a un objeto,
# que tienen todos los objetos del mismo tipo de dato.
#
# Para estas existe la sintaxis objeto.método(),
# en lugar del acostumbrado función(objeto)
#
# En este script vemos el método split() de los str (texto),
# que parte el texto en los espacios y devuelve una lista.

import random

frase = input()

palabras = frase.split()
print('Lista de palabras:')
print(palabras)

random.shuffle(palabras)
print('Luego de shuffle:')
print(palabras)

