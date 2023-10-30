from math import sqrt
from functools import reduce

def primes(n):
    ps = []
    limit = int(n / 2) + 1     # Límite es n / 2
    p = 2                      # El primer primo es 2
    while p <= limit:
        while n % p == 0:
            ps += [p]
            n = n // p
        # Mientras p tenga un divisor en ps
        while any([p % k == 0 for k in ps]):
            p += 1
        # Si no es, avanzamos
        if not n % p == 0:
            p += 1
    return [1] + ps


def dividers(N):
    # Obtiene la lista de primos y los multiplica sucesivamente de der a izq
    ps = primes(N)
    ds = [1] + [reduce(lambda a, b: a * b, ps[-n-1:]) for n in range(len(ps)-2) ]
    return ds

def testPrimes(n):
    assert reduce(lambda a,b: a*b, primes(n)) == n

def testDividers(n):
    assert not any([n % d != 0 for d in dividers(n)])
