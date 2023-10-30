
secuencia = [9,7,5,3,1]

suma = sum(secuencia)
cantidad = len(secuencia)

valida = int(suma/cantidad) - suma/cantidad == 0

if valida:
    print('Es una secuencia de ' + str(int(suma/cantidad)) + ' objetos')
else:
    print('Secuencia imposible!')

catches = [0] * cantidad

i = 0
for lanzamiento in secuencia:
    
    print(str(lanzamiento) + ' cae en ' + str((lanzamiento+i) % cantidad))
    
    if catches[(lanzamiento+i) % cantidad] == 0:
        catches[(lanzamiento+i) % cantidad] = 1
    else:
        print('Inválida!')
    i += 1


print(catches)
if sum(catches) == cantidad:
    print('Válida')
