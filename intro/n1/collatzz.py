from random import randint
from time import time, sleep

i = 0
n = randint(10000, 100000)

print(f'El número elegido es {n}...')

t0 = time()
while not(n == 1):
    if n % 2 == 0:
        n = n / 2   # n /= 2
    else:
        n = 3 * n + 1
    print(n)
    i += 1
    sleep(0.1)
t1 = time()

print(f'Terminado en {i} intentos en {t1-t0} segs')
