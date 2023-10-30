from time import sleep
from random import randint
from mapa import dibujar, saltar
from batalla import batalla, jugador, enemigo

# Clase 8 - Diccionarios

def progresivo(texto):
    for letra in texto:
            print(letra, end='')
            sleep(0.01)
    print()
    sleep(1)



en_paz = False

def hogar():
    saltar(-200, 0)
    if en_paz:
        progresivo("Estás en tu hogar.")
        progresivo("Aquí empezó todo.")
        progresivo("Ahora comprendés.")
        print()
        progresivo("The end")
    else:
        progresivo("Las frías paredes te oprimen.")
        progresivo("Una congoja existencial te agravia.")
        progresivo("Debés salir a la aventura.")

def bosque():
    saltar(-100, 70)
    progresivo("La tupida arboleda te proteje.")
    progresivo("Pero las criaturas acechan por la noche...")
    progresivo("Pasarás aquí la noche? [s/n]")
    opcion = input("> ")
    while opcion not in ['s', 'n']:
        opcion = input("> ")
    if opcion == 's':
        if randint(1, 100) < 50:
            progresivo("Una serpinte te muerde una nalga.")
            progresivo("-10HP")
            jugador['hp'] -= 10
        else:
            progresivo("La noche pasa sin mayores problemas...")
            progresivo("Lo que no te mata te fortalece.")
            progresivo("+5Atk")
            jugador['acumulado'] += 5

def aldea():
    saltar(50, 30)
    progresivo("El cálido ronroneo del ajetreo cotidiano.")
    progresivo("Deseas comprar algo?...")
    print("[No implementado, quejarse con el desarrollador]")

def rio():
    saltar(0, -50)
    progresivo("El suave arruyo de las venas de la tierra restaura toda tu vitalidad.")
    jugador['hp'] = jugador['hp_max']

def montaña():
    global en_paz
    saltar(140, 0)
    progresivo("No tan rápido.")
    progresivo("La montaña es sagrada.")
    progresivo("El lobo Fermín la guarda.")
    progresivo("Prueba tu valía o muere.")
    resultado = batalla(jugador, enemigo)
    if resultado == -1:
        progresivo("Más allá de los valles y ríos, fría y hostil, la cima del mundo.")
        progresivo("Contemplás el atardecer en silencio.")
        progresivo("Alcanzás la sabiduría.")
        progresivo("Podés volver en paz.")
        en_paz = True
    if resultado == 0:
        progresivo("Fermín se retira, pero has quedado sin fuerzas.")
        progresivo("Tenés que recuperar tus fuerzas antes de volver a intentarlo.")
    if resultado == 1:
        progresivo("Fermín te destrozó.")
        progresivo("No hay sensatez en quien no sabe retirarse a tiempo.")
        print()
        progresivo("Game over")
        quit()

mapa = {
'hogar'     : {
    'caminos'   : ['bosque', 'rio'],
    'acciones'  : hogar,
    'posicion'  : (-200, 0)
    },
'bosque'    : {
    'caminos'   : ['hogar', 'aldea'],
    'acciones'  : bosque,
    'posicion'  : (-100, 70)
    },
'aldea'     : {
    'caminos'   : ['montaña', 'bosque', 'rio'],
    'acciones'  : aldea,
    'posicion'  : (50, 30)
    },
'rio'       : {
    'caminos'   : ['hogar', 'aldea'],
    'acciones'  : rio,
    'posicion'  : (0, -50)
    },
'montaña'   : {
    'caminos'   : ['aldea'],
    'acciones'  : montaña,
    'posicion'  : (140, 0)
    }
}

dibujar(mapa)

def etpa(lugar):
    print()
    accion = mapa[lugar]['acciones']
    accion()
    print()
    print('Elegí el próximo paso:')
    for opcion in mapa[lugar]['caminos']:
        print(opcion)
    proximo = input('> ')
    while proximo == '':
        proximo = input('> ')
    etpa(proximo)


etpa('hogar')
