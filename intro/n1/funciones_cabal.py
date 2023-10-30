from random import randint

# Clase 7 - Práctica

# Cuando una función no tiene ningún
# efecto se llama pura o transparente

# Recibe: nada
# Devuelve: booleano
# Efectos: ninguno
def moneda():
    return randint(1,2) == 1


# Recibe: int
# Devuelve: int
# Efectos: ninguno
def dn(n):
    return randint(1,n)


# Recibe: string
# Devuelve: nada
# Efectos: printea un saludo a pantalla
def saludo(nombre):
    print(f'Hola {nombre}')


contador = 0  # Variable global

# Recibe: nada
# Devuelve: nada
# Efecto: incrementa la variable contador
def aumentar():
    global contador
    contador += 1

# Recibe: nada
# Devuelve: 10
# Efecto: ninguno
def lalala():
    mememe = 10  # Variable local
    return mememe



# Stack
def uno():
    return 1

def dos():
    return uno() + 1

def tres():
    return dos() * 2


# Factorial
def fact(n):
    if n > 1:
        return n * fact(n - 1)
    else:
        return 1
