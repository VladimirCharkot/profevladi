# Conjetura de Collatz

# Clase 3 - Hola while

num = int(input("Ingresá un número: "))

while num > 1:   # distinto de 1
    print(num)
    if num % 2 == 0:     # es par
        num = num / 2
    else:
        num = num * 3 + 1

print("Llegamos... 1")

# mientras el número no sea 1 repetir:
    # si el número es par, dividirlo por 2
    # si es impar, multiplicarlo por 3 y sumar 1
