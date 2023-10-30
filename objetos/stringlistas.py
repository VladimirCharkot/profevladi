texto = "anita lava la tina"

# Algunos MÉTODOS de strings:
print()
print(f'Texto: {texto}')
print(f'Cantidad de veces que aparece la letra a: {texto.count("a")}')
print(f'Texto capitalizado: {texto.capitalize()}')
print(f'Texto pero a los gritos: {texto.upper()}')
print(f'Texto centrado en 40 caracteres: {texto.center(40)}')
print(f'Posición de la letra "v" dentro del texto: {texto.index("v")}')
print(f'Texto pero en burla: {texto.replace("a","i")}')
print(f'El texto termina con ina?: {texto.endswith("ina")}')
print(f'El texto termina con e?: {texto.endswith("e")}')
print(f'Palabras del texto: {texto.split()}')
print(f'Texto: {texto}')
print()

palabras = texto.split()

# Algunos MÉTODOS de listas:
print(f'Palabras: {palabras}')
print('Agregando un elemento a la lista...')
palabras.append("rápida")
print('Extendiendo la lista con otra...')
palabras.extend(["y","graciosamente"])
print('Ordenando la lista...')
palabras.sort()
print('Invirtiendo el orden')
palabras.reverse()
print(f'Palabras: {palabras}')
print()

print(f'Las joineamos: {"_".join(palabras)}')

# Los strings NO MUTAN, las listas SÍ
