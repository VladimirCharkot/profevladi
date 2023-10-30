#!/usr/bin/python3
# -*- encoding: utf-8 -*-

# Repeticiones, ciclos, bucles, loops... son todos términos que designan los mismo

print('Cantidad fija de repeticiones:')
for i in range(5):
    print('Número ' + str(i))

# En todo ciclo hay un patrón base que se repite y una parte que varía de iteración en iteración

print()
print('Expresión que cambia con i:')
for i in range(5):
    print(str(i) + ' al cuadrado: ' + str(i*i))

# La forma general es
# for [variable] in [secuencia]:
#   [instrucciones]
# Recordando que la indentación es importante

print()
texto = 'Vida verdadera es la que se vive con la certeza nítida de estar viviéndola'

largo = len(texto)
for i in range(largo):
    print(texto[largo-i-1], end='')
print()

# (Recordando que con corchetes accedemos al elemento enésimo de una secuencia:
# print('Vida'[1])
# > i
# y recordando que el índice empieza a contar en 0 y no en 1)


# Encriptación muy básica:

# La función ord() toma un caracter y devuelve el número que le corresponde en la tabla ascii:
# print(ord('a'))
# > 97

# La función chr() toma un número de la tabla ascii y devuelve el caracter que le corresponde:
# print(chr(97))
# > a

print()
encriptado = ''
for letra in texto:
    encriptado = encriptado + chr(ord(letra) + 1)

print(encriptado)

# Aplicamos un desplazamiento de un lugar a cada letra. Esto se rompe un poco con las letras con tilde porque están fuera de ascii... pero no implica que no podamos recuperar el texto encriptado:

print()
for letra in encriptado:
    print(chr(ord(letra) - 1), end='')
