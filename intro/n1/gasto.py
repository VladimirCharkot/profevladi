
# Recibe cantidad de viajes
# y devuelve tarifa total

def gasto(cant_viajes):
    # Calculo la tarifa total sin descuento
    precio_base = 30
    precio_normal = precio_base * cant_viajes

    # Según la cantidad de viajes aplico el descuento
    # multiplicando por 80% (0.8), 70% (0.7) o 60% (0.6)
    if cant_viajes > 0 and cant_viajes <= 20:
        return precio_normal

    if cant_viajes >= 21 and cant_viajes <= 30:
        # si algo le descuento 20% me queda el 80%
        return precio_normal * 0.8

    if cant_viajes >= 31 and cant_viajes <= 40:
        return precio_normal * 0.7

    return precio_normal * 0.6



assert(gasto(0) == 0)
assert(gasto(1) == 30)
assert(gasto(20) == 600)
assert(gasto(21) == 504)
assert(gasto(30) == 720)
assert(gasto(31) == 651)
##assert(gasto(40) == )
##assert(gasto(41) == )
##assert(gasto(100) == )


if gasto(0) != 0:
    print("Hay un error cuando llamo a gasto(0)")

if gasto(1) != 30:
    print("Hay un error cuando llamo a gasto(1)")

if gasto(31) != 651:
    print("Hay un error cuando llamo a gasto(651)")


numero_texto = input("Ingresá la cantidad de viajes de este mes: ")
numero = int(numero_texto)
gasto_total = gasto(numero)
print("Total gastado: " + str(gasto_total))
