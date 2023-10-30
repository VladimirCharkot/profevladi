from random import randint

# Clase 5 - Funciones

# Esta función no devuelve nada (no tiene return)
def jeringocear(texto):
    nuevo = ''
    for letra in texto:
        if letra in 'aeiou':
            nuevo = nuevo + letra + 'p' + letra
        else:
            nuevo = nuevo + letra
    print(nuevo)

# Esta función devuelve un texto
def leer_seguro():
    ingresado = input("Ingresá texto: ")
    while ingresado == '':
        ingresado = input("Ingresá texto: ")
    return ingresado

# Esta función devuelve un número
def d6():
    return randint(1,6)

# Esta función devuelve una lista
def cincod6():
    l = []
    for i in range(5):
        l = l + [randint(1,6)]
    return l

# Esta función recibe una frase y una letra
# y devuelve un número correspondiendo a la
# cantidad de veces que aparece la letra
def contarletra(frase, letra):
    cuantas = 0
    for l in frase:
        if l == letra:
            cuantas = cuantas + 1
    return cuantas

# Esta función recibe una frase y devuelve
# una lista conteniendo en cada posición la
# cantidad de veces que aparece cada vocal
def contar_vocales(frase):
    cant_a = contarletra(frase, 'a')
    cant_e = contarletra(frase, 'e')
    cant_i = contarletra(frase, 'i')
    cant_o = contarletra(frase, 'o')
    cant_u = contarletra(frase, 'u')
    return [cant_a, cant_e, cant_i, cant_o, cant_u]

# Recibe base y altura y devuelve superficie
def superficie_triangulo(base, altura):
    return base * altura / 2


# Lee una password del usuario hasta 3 veces
# y devuelve True si es correcta y False sino
def login():
    passwd = input("Ingresá tu contraseña > ")
    intentos = 1

    while passwd != '4dm1n' and intentos < 3:
        passwd = input("Ingresá tu contraseña > ")
        intentos = intentos + 1

    if passwd == 'admin':
        return True
    else:
        return False

# Recibe 3 números representando las longitudes
# de tres lados y devuelve True si pueden
# formar un triángulo
def es_triangulo(a, b, c):
    return a != 0 and b != 0 and c != 0 and a + b > c and a + c > b and b + c > a


print("Hola hola! Este es el script de las funciones")
print("Definimos un montón de funciones y ahora las vamos a usar")
print("Mirá ingresame un texto y te lo jeringoceo")

texto_1 = input("> ")
print(jeringocear(texto_1))

print('Mirá te hago una tirada de generala')
print(cincod6())

print("Ingresame una frase que te cuento las vocales dale")
texto_2 = input("> ")
print(contar_vocales(frase))

print("A ver si te sabés la pass...")

if login():
    print("Buena. Sabés donde mirar.")
    print("Te ganaste la posibilidad de ingresar tres números y ver si forman triángulo")
    l1 = float(input("Ingresá el primero"))
    l2 = float(input("Ingresá el segundo"))
    l3 = float(input("Ingresá el tercero"))
    if es_triangulo(l1, l2, l3):
        print("Forma triángulo!")
    else:
        print("No forma triángulo")
else:
    print("NO! (╯°□°）╯︵ ┻━┻")

print("ಠ‿ಠ")
