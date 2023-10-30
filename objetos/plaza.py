from random import sample, randint

class Persona():

    def __init__(self, nombre, intereses, desintereses):
        self.nombre = nombre
        self.intereses = set(intereses)
        self.desintereses = set(desintereses)

    def __str__(self):
        return f'{self.nombre}'
    
    def __repr__(self):
        return self.__str__()

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre}, mis intereses son {self.intereses}, y mis desintereses son {self.desintereses}')

    def saludar_a(self, a_quien):
        print('Hola ' + a_quien.nombre + ', me llamo ' + self.nombre)

    def afinidad(self, otra_persona):
        aff = 0
        intereses_en_comun = self.intereses & otra_persona.intereses
        desintereses_en_comun = self.desintereses & otra_persona.desintereses
        intereses_cruzados_1 = self.intereses & otra_persona.desintereses
        intereses_cruzados_2 = self.desintereses & otra_persona.intereses
        aff += len(intereses_en_comun)
        aff += len(desintereses_en_comun)
        aff -= len(intereses_cruzados_1)
        aff -= len(intereses_cruzados_2)
        return aff


class Grupo():
    
    def __str__(self):
        return f'Grupo {self.personas}'

    def __repr__(self):
        return self.__str__()

    def __init__(self, personas):
        self.personas = personas
        self.intereses()
        self.desintereses()

    def mapa(self):
        m = {}
        for p1 in self.personas:
            for p2 in self.personas:
                if p1.nombre != p2.nombre:
                  m[f'{p1.nombre}-{p2.nombre}'] = p1.afinidad(p2)
        return m

    def saludar(self):
        for p in self.personas:
            p.saludar()

    def potencias(self):
        pots = {}                         # Diccionario!
        for i in self.intereses():
            pots[i] = intereses.count(i)  # Métodos de listas!
        return pots

    def intereses(self):
        # Juntamos todos los intereses:
        intereses = []
        for pers in self.personas:
            intereses.extend(pers.intereses)
        return set(intereses)

    def desintereses(self):
        # Juntamos todos los desintereses:
        desintereses = []
        for pers in self.personas:
            desintereses.extend(pers.desintereses)
        return set(desintereses)

class Plaza():

    def __init__(self, grupos, nombre):
        self.grupos = grupos
        self.nom = nombre

    def __str__(self):
        return 'Plaza ' + self.nom

    def __repr__(self):
        return '> ' + self.__str__()

    def __add__(self, otra_plaza):
        todes_les_amis = self.grupos + otra_plaza.grupos
        nuevo_nombre = self.nom[:3] + otra_plaza.nom[-3:]
        return Plaza(todes_les_amis, nuevo_nombre)


# *-*-*-*-*-*-*-*-*-* Main! *-*-*-*-*-*-*-*-*-*

# Datos de prueba: 
nombres = ['vladi', 'lucho', 'sofi', 'martin', 'isaac', 'helena', 'carla', 'juana']

intereses = ['programacion', 'circo', 'skate', 'artes marciales', 'patín', 'teatro',
             'ilustración', 'filosofía', 'videojuegos', 'música', 'rap', 'danza', 'poesía']

# Generamos una persona por nombre, con intereses y desintereses al azar: 
personas = []                                       # Empezamos con una lista vacía
for nombre in nombres:
    intereses = sample(intereses, 5)                # Tomamos 5 intereses al azar
    corte = len(intereses) // 2 +  randint(0, 2)    # Partimos esa lista en dos:
    persona = Persona(nombre, intereses[:corte], intereses[corte:])
    personas += [persona]                           # Agregamos la nueva persona a la lista de personas

corte = len(personas) // 2 + randint(-1, 1)
grupo_1 = Grupo(personas[:corte])
grupo_2 = Grupo(personas[corte:])

p = Plaza([grupo_1, grupo_2], 'Corneta')

juana = Persona('Juana', [ 'videojuegos', 'música' ], [ 'programacion', 'circo' ])
carlos = Persona('Carlos', [ 'programacion', 'circo' ], [ 'música' ])