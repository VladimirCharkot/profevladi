pwd = 'juli'
n = 0

intento = input('Ingresá la password: ')

while not(intento == pwd):
    n = n + 1
    intento = input('Error, intentá de vuelta: ')
    print('Van ' + str(n) + ' intentos')

print('Bienvenide! c:')
