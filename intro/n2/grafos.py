estructura = {
    'inicio' : ['galletitas', 'manzanas'],
    'galletitas' : ['tunel', 'escape'],
    'manzanas' : ['escape', 'peluqueria'],
    'tunel' : ['salida'],
    'escape' : ['laberinto', 'refugio'],
    'peluqueria' : ['refugio'],
    'refugio' : ['salida'],
    'laberinto' : ['salida']
}

textos = {
    'inicio' : 'Estábamos con la banda en el cente',
    'galletitas' : 'El lucho peló unas traviata',
    'manzanas' : 'Había una piba comiendo unas manzanas',
    'tunel' : 'Nos fuimos a tomar el subte y se quedó entre dos estaciones',
    'escape' : 'Salimos corriendo por el portón de Diaz Velez',
    'peluqueria' : 'Dijo que venía corriendo de la peluquería que había sido invadida por mosquitos del tamaño de chancletas',
    'refugio' : "Nos refugiamos en Ugi's",
    'laberinto' : 'Entramos al subte por gallardo',
    'salida' : 'Nos comieron los zombies'    
}


# recursiva c:
def etpa(estado):
    print()
    print(textos[estado])
    print()
    if estado != 'salida':
        print('Elegí el próximo paso:')
        for opcion in estructura[estado]:
            print(opcion)
        proximo = input()
        etpa(proximo)
    else:
        print('Fin c:')


etpa('inicio')

