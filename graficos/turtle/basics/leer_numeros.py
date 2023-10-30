cantidad = 0
suma = 0

ingresado = input('Número > ')

while not(ingresado == ''):
    n = int(ingresado)
    cantidad += 1
    suma += n
    ingresado = input('Número > ')
    
print(f'El promedio es: {suma/cantidad}')
