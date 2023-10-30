n = 0
suma = 0

print('Dame cinco números y te'\
      + 'calculo el promedio')

while n < 5:
    numerito = int(input('Ingresá un numerito: '))
    suma = suma + numerito
    n = n + 1
    print('Ahora la suma vale ' + str(suma))
    print('Van ' + str (n) + ' numeritos')

print('Terminamos')
print('El promedio es: ' + str(suma/n))
