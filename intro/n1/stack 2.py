def hola(numero):
    if numero > 0:
        print(numero)
        hola(numero-1)
    print(":D")

hola(2)
