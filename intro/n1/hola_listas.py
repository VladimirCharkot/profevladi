# Creamos una lista
nombres = ['juli', 'vladi', 'python']

print(f'Primero {l[0]}')
print(f'Luego {l[1]}')
print(f'Y al final {l[2]}')

print()

for nom in nombres:
    print(f'Hola {nom}!')
    
print()

# Tenemos la función list que intenta
# convertirnos lo que le pasemos en una lista
nums = list(range(10))
print(f'Acá tenés los números del 0 al 9: {nums}')

print()

# Si a la izquierda de una asignación ponemos
# la misma cantidad de variables que haya en
# una colección a la derecha de la asignación,
# podemos "desempacar" los valores
j, v, p = nombres
print(f'j: {j}')
print(f'v: {v}')
print(f'p: {p}')

print()

# Además de listas tenemos tuplas, que son lo
# mismo pero no pueden ser mutadas:

tupla = ('hola', 'wachis', 'piolas')
# tupla[0] = 'chau' <-- Error!

# En cambio a las listas sí las podemos mutar:
nombres[2] = 'processing'

print('Nombres luego de mutar: {nombres}')

print()

# También podemos consultar si un valor está
# en una colección con el operador in:

tiene_juli = 'juli' in nombres
print('Nombres tiene a "juli": {tiene_juli}')

tiene_python = 'python' in nombres
print('Nombres tiene a "python": {tiene_python}')

