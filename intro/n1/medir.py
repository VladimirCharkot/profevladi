from time import time

# Clase 7 - Práctica

def medir(funcion):
    t0 = time()
    funcion()
    t1 = time()
    print(f'Tardó en correr {t1-t0}s')


def combinaciones():
    abc = 'abcdefghijklmnñopqrstuvwxyz'
    passwords = []

    for letra1 in abc:
        for letra2 in abc:
            for letra3 in abc:
                for letra4 in abc:
                    for letra5 in abc:
                        passwords += [letra1 + letra2 + letra3 + letra4 + letra5]


medir(combinaciones)
