from time import sleep
import sys

# Escribe un texto progresivamente
def progresivo(texto):
    for letra in texto:
            print(letra, end='')
            sleep(0.02)
            sys.stdout.flush()  # vaciar el buffer
    sleep(1)
    print()

# Recibe una lista de opciones y ofrece un menú
def menu(opciones):
    progresivo("Qué hacer?")
    i = 0
    for opcion in opciones:
        i += 1
        progresivo(f'{i} - {opcion}')
    eleccion = int(input("> "))
    while eleccion < 1 and eleccion > i:    # volvemos a leer mientras inválida
        eleccion = int(input("> "))
    return eleccion

# Lee solo sí o no, devuelve True o False
def menu_sn(pregunta):
    progresivo(pregunta + " [s/n]")
    opcion = input("> ")
    while opcion not in ['s', 'n']:
        opcion = input("> ")
    return opcion == 's'



en_paz = False
tiene_llave = False
tiene_album = False
noche_bosque = False
tiene_dinero = False
tiene_viveres = False
visito_aldea = False
visito_montaña = False

def hogar():
    global tiene_album
    if en_paz:
        progresivo("Estás en tu hogar.")
        progresivo("Ya no es tan solo tu casa.")
        progresivo("Aquí empezó todo.")
        progresivo("Ahora comprendés.")
        print()
        progresivo("The end")
        exit()
    else:
        progresivo("Te encontrás en tu casa.")
        progresivo("Las frías paredes te oprimen.")
        progresivo("Una congoja existencial te agravia.")
        progresivo("Debés salir a la aventura.")
        opcion = menu(["Salir al mundo", "Revisar la casa"])
        if opcion == 2:
            if not tiene_llave:
                progresivo("Un viejo cajón cerrado.")
                progresivo("Con llave.")
                progresivo("Qué tenía?...")
                progresivo("Lo olvidaste...")
            else:
                progresivo("Con la llave abrís el viejo cajón cerrado.")
                progresivo("Un álbum de fotos.")
                progresivo("Reconocés en algunas a tu madre.")
                progresivo("Hay otras personas que no reconocés.")
                progresivo("[Obtenido: Antiguo álbum de fotos]")
                tiene_album = True


def bosque():
    global tiene_viveres
    global noche_bosque
    progresivo("La tupida arboleda te proteje.")
    progresivo("Pero las criaturas acechan por la noche...")
    if menu_sn("Pasarás aquí la noche?"):
        if tiene_viveres:
            progresivo("Los animales del bosque se comen tus víveres por la noche")
            tiene_viveres = False
        else:
            progresivo("Amanecés con dolor de espalda, pero sin mayores problemas")
        noche_bosque = True
    else:
        progresivo("La sobria cordura de retirarse a tiempo.")
        if visito_montaña:
            progresivo("En el camino de salida encontrás árboles frutales.")
            progresivo('[Obtenido: Frutas frescas]')
            tiene_viveres = True
        progresivo("Nutrís tu alma con sonidos de pajaritos y seguís viaje.")

def aldea():
    global tiene_viveres
    global tiene_dinero
    global visito_aldea
    progresivo("El cálido ronroneo del ajetreo cotidiano.")
    progresivo("Alguien se te aproxima...")
    if noche_bosque and not visito_aldea:
        progresivo('- "Eh! Te ví durmiendo en el bosque anoche!"')
        progresivo('"...qué admirable valentía!"')
        progresivo('"...puedo ayudarte en algo?"')
        opcion = menu(['"Estoy buscando una aventura"', '"Necesito comprar víveres"', '"En nada, adiós!"'])
        if opcion == 1:
            progresivo('"Conozco muchas personas que se encontraron consigo mismas en la montaña..."')
            progresivo('"...quizás debas ir para allá"')
            progresivo('"Está pasando el río"')
        if opcion == 2:
            progresivo('"La tienda de la aldea está cerrada..."')
            progresivo('"...pero te puedo ofrecer un poco de mi alimento"')
            progresivo('[Obtenido: Pan de semillas y cantimplora con agua]')
            tiene_viveres = True
        progresivo('"Adiós!"')
    else:
        if visito_aldea and not(menu_sn("Un vendedor, querés hablarle?")):
            return
        progresivo('- "Buenas buenas!"')
        progresivo('"...mi nombre es Arturo Laercio..."')
        progresivo('"...soy comerciante."')
        progresivo('"Si deseas comprar víveres o herramientas viniste al lugar correcto..."')
        opcion = menu(['"No entiendo nada de lo que está pasando"', '"Necesito comprar víveres"', '"Nada, adiós"'])
        if opcion == 1:
            progresivo('"Quizás deberías ir a sentarte al río en silencio."')
            progresivo('"Eso me ayuda sobremanera cuando me siento confundido."')
        if opcion == 2:
            progresivo('"Perfecto! Tengo bananas, estofado y pan de lembas"')
            progresivo('"También cantimploras con agua"')
            if tiene_dinero:
                progresivo('"Aunque por esa cantidad puedo ofrecerte solo frutas y agua..."')
                progresivo('[Obtenido: Frutas y cantimplora con agua]')
                tiene_viveres = True
                tiene_dinero = False
                progresivo('"Buen viaje!"')
            else:
                progresivo('"Qué? No tenés dinero?"')
                progresivo('"Jajajajaja adiós"')
    visito_aldea = True

def rio():
    global tiene_llave
    global tiene_viveres
    global tiene_dinero
    progresivo("El agua fluye.")
    progresivo("La floresta exhubera.")
    progresivo("La vida medra.")
    opcion = menu(['Explorar las márgenes del río', 'Sentarse en silencio junto a la corriente', 'Zambullirse en el agua', 'Irse'])
    if opcion == 1:
        progresivo("Seguís el sendero.")
        progresivo("Se interna en el bosque.")
        if tiene_llave:
            progresivo("En un área retirada encontrás un manzano")
            progresivo('[Obtenido: Manzanas frescas]')
            tiene_viveres = True
        else:
            progresivo("Al final del camino se ve una cabaña")
            if menu_sn("Vas a golpear?"):
                progresivo("Un anciano abre la puerta.")
                progresivo("Sus ojos se abren redondos de sorpresa.")
                progresivo("Te conoce!")
                progresivo('- "Sabía que te volvería a ver!"')
                progresivo('"Soy el tío de tu madre"')
                progresivo('"Eras así de pequeño la última vez que nos vimos."')
                progresivo('"Lamento mucho su partida."')
                progresivo('"Tengo algo para tí, que ella quería que te diera, y que me dió para que cuidara."')
                progresivo('[Obtenido: Vieja llave]')
                tiene_llave = True
                progresivo('"Tú sabes qué es lo que abre."')
                progresivo('"Dentro hay algo muy especial."')
                progresivo('"Debes llevarlo a la montaña."')
                progresivo('"No tiene sentido que de más explicaciones."')
                progresivo('"Hazlo y verás."')
                progresivo('"Buen viaje!"')
            else:
                progresivo("En el camino de regreso encotrás algunas monedas en suelo.")
                progresivo("[Obtenido: Dinero]")
                tiene_dinero = True
    if opcion == 2:
        progresivo("El suave arruyo de las venas de la tierra restaura tu claridad.")
        progresivo("Qué es realmente importante?")
        progresivo("El viejo cajón de tu casa viene a tu mente.")
        progresivo("Por qué aquí?")
        progresivo("Por qué ahora?")
    if opcion == 3:
        progresivo("El abrazo del agua te revitaliza.")
        if not tiene_dinero:
            progresivo("Ves algo cerca de la orilla.")
            progresivo("Son monedas!")
            progresivo("[Obtenido: Dinero]")
            tiene_dinero = True

def montaña():
    global en_paz
    progresivo("No tan rápido.")
    progresivo("La montaña infunde un temible respeto.")
    progresivo("No deberías aventurarte sin la debida preparación.")
    if menu_sn("Vas a intentarlo?"):
        if not tiene_viveres:
            progresivo("Luego de algunas horas de caminar perdés el sendero.")
            progresivo("Algunas horas pasan y no das rumbo cierto.")
            progresivo("El hambre y la sed te aplastan.")
            progresivo("Quién se interna en la montaña sin víveres ni agua?")
            progresivo("No hay sensatez en quien no sabe retirarse a tiempo.")
            progresivo("Fin :(")
            exit()
        else:
            progresivo("Más allá de los valles y ríos, fría y hostil, la cima del mundo.")
            if tiene_album:
                progresivo("Hay otra persona!")
                progresivo("Se te aproxima")
                progresivo('"Ese álbum..."')
                progresivo('"...vos debés ser..."')
                progresivo('"...mi nieto!"')
                progresivo("Tu abuelo te cuenta la historia de su separación de su hermano y de tu madre antes de que nacieras.")
                progresivo("Entendés tu origen.")
                progresivo("Se disuelve la duda.")
                progresivo("Contemplás el atardecer en silencio.")
                progresivo("Alcanzás la sabiduría.")
                progresivo("Podés volver en paz.")
                en_paz = True
            else:
                progresivo("Hay una cabaña...")
                progresivo("...está vacía")
                # QUITAR COMIDA
    else:
        if not tiene_viveres:
            progresivo("BIEN.")
            progresivo("No es sensato internarse en la montaña sin agua ni víveres")

mapa = {
    'hogar'     : {
        'caminos'   : ['bosque', 'rio'],
        'acciones'  : hogar
    },
    'bosque'    : {
        'caminos'   : ['hogar', 'aldea'],
        'acciones'  : bosque
    },
    'aldea'     : {
        'caminos'   : ['montaña', 'bosque', 'rio'],
        'acciones'  : aldea
    },
    'rio'       : {
        'caminos'   : ['hogar', 'aldea'],
        'acciones'  : rio
    },
    'montaña'   : {
        'caminos'   : ['aldea'],
        'acciones'  : montaña
    }
}


def visitar(lugar):
    print()
    accion = mapa[lugar]['acciones']    # Agarramos la funcion de ese lugar
    accion()                            # La invocamos
    print()
    print('Elegí el próximo paso:')
    opciones = mapa[lugar]['caminos'] + [lugar]
    for opcion in opciones:
        print(opcion)
    proximo = input('> ')
    while proximo not in opciones:
        proximo = input('> ')
    visitar(proximo)


visitar('hogar')
