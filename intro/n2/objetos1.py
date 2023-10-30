import random


def rolar_dados(n, dado):
    l = []
    for i in range(n):
        tirada = random.randint(1,dado)
        l.append(tirada)
    l.sort()
    return l

def tirar(tirada):
    componentes = tirada.split('d')
    cantidad = int(componentes[0])
    dado = int(componentes[1])
    resultados = rolar_dados(cantidad, dado)
    return resultados


class Equipo:

    def __init__(self, peso):
        self.peso = peso


class Arma(Equipo):

    def __init__(self, dmg, peso):
        super().__init__(peso)
        self.dmg = dmg

    def __str__(self):
        return f'Arma de {self.dmg} atk y {self.peso} peso'


class Escudo(Equipo):

    def __init__(self, dfs, peso):
        super().__init__(peso)
        self.dfs = dfs
        
    def __str__(self):
        return f'Escudo de {self.dfs} def y {self.peso} peso'

    def __gt__(self, otro):
        return self.peso > otro.peso

    def __add__(self, otro):
        return Escudo(self.dfs + otro.dfs, self.peso + otro.peso)
    

class Personaje:

    def __init__(self, nombre_p, hp_p):
        self.nombre = nombre_p
        self.hp = hp_p
        self.arma = None
        self.escudo = None
        self.carga = 0

    def equipar(self, equipo):
        if type(equipo) == Arma:
            self.arma = equipo
        if type(equipo) == Escudo:
            self.escudo = equipo
        print(f'Equipado {equipo}')

    def saludar(self):
        print(f'''Hola, mi nombre es {self.nombre} y tengo {self.hp} hp''')

    def atacar(self, otro_personaje):
        if self.puedo_atacar():
            #print(f'{self.nombre} atacando')
            if self.arma:
                otro_personaje.hp -= sum(tirar(self.arma.dmg))
            else:
                otro_personaje.hp -= sum(tirar('1d3'))
            self.carga = self.peso_total()
        #else:
            #print(f'{self.nombre} recargando')

    def vive(self):
        return self.hp > 0

    def puedo_atacar(self):
        self.carga -= 1
        return self.carga <= 0

    def peso_total(self):
        total = 0
        if self.escudo:
            total += self.escudo.peso
        if self.arma:
            total += self.arma.peso
        return total


ramon = Personaje('Ramón', 50)
julian = Personaje('Julián', 90)

espada = Arma('3d6', 20)
katana = Arma('2d6', 10)

arco = Arma('3d4', 15)
ballesta = Arma('2d4', 15)

escudo_madera = Escudo(5, 15)
escudo_acero = Escudo(15, 50)

ramon.equipar(espada)
ramon.equipar(escudo_madera)

julian.equipar(katana)
julian.equipar(escudo_madera)


while ramon.vive() and julian.vive():
    ramon.atacar(julian)
    julian.atacar(ramon)

ramon.saludar()
julian.saludar()
