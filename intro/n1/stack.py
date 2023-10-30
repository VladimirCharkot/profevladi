def comentario():
    print("Tanto tiempo!")

def pregunta():
    print("Todo bien?")

def saludo(nombre):
    if len(nombre) > 4:
        print("Hola " + nombre + "!")
        comentario()
    else:
        print("Kace " + nombre + "!")
    pregunta()
    print()


saludo("Lore")
saludo("Vladi")
