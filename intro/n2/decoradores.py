from time import time, sleep

def medir(funcion):
    def medir_tiempo(*args):
        t0 = time()
        r = funcion(*args)
        t1 = time()
        print(f'La funcion tardó {round(t1-t0, 3)} segs en ejecutarse')
        return r
    return medir_tiempo


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

@medir
def dormir(n):
    sleep(n)

@medir
def fibo_34():
    print(fibonacci(34))

fibo_34()
