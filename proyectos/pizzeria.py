print()
print("Les damos la bienvenida a pyzzería! 🍕😋")
print()
print("Por favor indíquenos su orden:")

total = 0

pizzas = 0
bebidas = 0
postres = 0

# Leemos antes de entrar al while
print("1 - Pedir pizza  🍕 ($50 + adicionales)")
print("2 - Pedir bebida 🍺 ($14 / $20 / $25)")
print("3 - Pedir postre 🍨 ($20 / $40 / $50)")
print("4 - Listo! Orden finalizada")

opcion = input("> ")
while opcion not in "1234":
    print("Ingrese una opción válida")
    opcion = input("> ")

while opcion != "4":

    if opcion == "1":

        pizzas += 1
        total += 50

        print("Le ponemos tomate? (+$10) [s/n]")
        sn = input("> ")
        if sn == 's':
            total += 10

        print("Le ponemos rúcula? (+$8) [s/n]")
        sn = input("> ")
        if sn == 's':
            total += 8

        print("Le ponemos huevo? (+$5) [s/n]")
        sn = input("> ")
        if sn == 's':
            total += 5

    if opcion == "2":
        print("1 - Agua ($14)")
        print("2 - Gaseosa ($20)")
        print("3 - Cerveza ($25)")

        bebidas += 1

        bebida = input("> ")
        while bebida not in "123":
            print("Ingrese una opción válida")
            bebida = input("> ")

        if bebida == "1":
            total += 14

        if bebida == "2":
            total += 20

        if bebida == "3":
            total += 25


    if opcion == "3":
        print("1 - Galleta ($20)")
        print("2 - Flan ($40)")
        print("3 - Helado ($50)")

        postres += 1

        postre = input("> ")
        while postre not in "123":
            print("Ingrese una opción válida")
            postre = input("> ")

        if postre == "1":
            total += 20

        if postre == "2":
            total += 40

        if postre == "3":
            total += 50


    # Volvemos a leer al final del while
    print()
    print("Algo más?")
    print("1 - Pedir pizza")
    print("2 - Pedir bebida")
    print("3 - Pedir postre")
    print("4 - Orden lista!")
    opcion = input("> ")
    while opcion not in "1234":
        opcion = input("> ")

print()
if pizzas or bebidas or postres:
    print("Su orden cuenta con:")
    if pizzas:
        print(pizzas, "pizzas")
    if bebidas:
        print(bebidas, "bebidas")
    if postres:
        print(postres, "postres")

    print()
    print("Son $", total)
    print()
    print("Gracias! Vuelvas prontos!")

else:

    print("Gracias por su consulta!")
