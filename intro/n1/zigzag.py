# Clase 3 - Hola while

n = 0

while n < 50:
    n = n + 1
    if n % 3 == 0 and n % 5 == 0:
        print('Zig-zag!')
    elif n % 3 == 0 and n % 5 != 0:
        print('Zig')
    elif n % 3 != 0 and n % 5 == 0:
        print('Zag')
    else:
        print(n)
