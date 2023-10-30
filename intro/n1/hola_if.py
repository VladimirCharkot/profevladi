edad = int(input("ingresá una edad > "))

# Clase 2 - Condicionales

if edad < 3:
    print("Es bebé")
elif edad < 10:
    print("Es niñx")
elif edad < 20:
    print("Es adolescente")
elif edad < 60:
    print("Es adultx")
else:
    print("Es ancianx")

print("Saludos!")


if edad < 3:
    print("Es bebé")
else:
    if edad < 10:
        print("Es niñx")
    else:
        if edad < 20:
            print("Es adolescente")
        else:
            if edad < 60:
                print("Es adultx")
            else:
                print("Es ancianx")

print("Saludos!")
