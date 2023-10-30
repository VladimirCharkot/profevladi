def leer_numeros():
    l = []
    n = input('ingresa numeros enteros')

    while n != '':
        l = l + [int(n)]
        n = input('ingresa numeros enteros')

    return l
        

def max_min(f):
    minimo = f[0]
    maximo = f[0]

    for i in f:
        print(i)
        if i < minimo:
            minimo = i
        if i > maximo:
            maximo = i
            
    return [maximo, minimo]

nums = leer_numeros()
mm = max_min(nums)
print(f"Max: {mm[0]}")
print(f"Min: {mm[1]}")
