from random import randint

# Clase 4 - Hola listas

user = input("[P]iedra, pape[l] o [t]ijera? (p|l|t) > ")

compu_n = randint(0,2)

opciones = ['p', 'l', 't']
nombres = ['piedra', 'papel', 'tijera']

compu = opciones[compu_n]
print("La compu sacó", nombres[compu_n])



if user == compu:
    print("Empate")
else:
    gano_user = (user == 'p' and compu == 't') or\
                (user == 'l' and compu == 'p') or\
                (user == 't' and compu == 'l')
    if gano_user:
        print("Ganaste")
    else:
        print("Perdiste")
