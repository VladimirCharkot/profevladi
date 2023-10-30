def saludar():
    nombre = input("Ingresá tu nombre: ")
    cantidad_texto = input("Cuantas veces querés verlo? ")
    cantidad = int(cantidad_texto)
    print((nombre + '\n') * cantidad)

saludar()
