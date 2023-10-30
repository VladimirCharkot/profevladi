# Variables globales
# Para asignarles un valor desde dentro de una función
# hay que declararlas con la instrucción global
visito_montaña = False

def hogar():
    if visito_montaña:
        print("Tu casa ahora es tu hogar")
        print("Fin")
        exit()
    else:
        print("Estamos en casa")

def bosque():
    print("Aquí es el bosque")

def aldea():
    print("Esto es la aldea")

def rio():
    print("Estamos en el río")

def montaña():
    print("La montaña")
    global visito_montaña
    visito_montaña = True


# Grafo
# Cada clave mapea a un diccionario con caminos y acciones.
# En 'caminos' ponemos una lista de lugares alcanzables desde este lugar. Todo elemento de estas listas tiene que estar en las claves de mapa, para que no pinche la función de más abajo.
# En 'acciones' ponemos la funcion que queremos que represente ese lugar.

#  Minimap:
#
#        bosque
#      /         \
# hogar          aldea - montaña
#      \         /
#        - rio -

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

# Esta función se encarga de traer a la vida el grafo
# Es recursiva :)
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
