from random import randint

# Python 2 - Paradigmas

class Equipo():

    def __init__(self, p_hp, p_atk):
        self.p_hp = p_hp
        self.p_atk = p_atk


class Arma(Equipo):

    def __init__(self, atk):
        super().__init__(0, atk)


class Amuleto(Equipo):

    def __init__(self, hp):
        super().__init__(hp, 0)


class Personaje():

    def __init__(self, nombre, hp_max, atk1, atk2):
        self.nombre = nombre
        self.hp = hp_max
        self.hp_max = hp_max
        self.atk1 = atk1
        self.atk2 = atk2
        self.adicional = 0

    def vivo(self):
        return self.hp > 0

    def atacar(self, otro):
        dmg = randint(self.atk1, self.atk2) + self.adicional
        otro.hp -= dmg

    def status(self):
        if self.hp < 0:
            self.hp = 0
        print(f' [{self.nombre}] : {self.hp}/{self.hp_max}HP')

    def equipar(self, equipo):
        self.hp += equipo.p_hp
        self.adicional += equipo.p_atk


class Jugador(Personaje):

    def atacar(self, otro):
        print("Qué hacer? [A]tacar, [H]uir, A[c]umular")
        accion = input("> ").lower()
        if accion == 'a':
            dmg = randint(self.atk1, self.atk2)
            otro.hp -= dmg
        elif accion == 'h':
            if randint(1,100) < 20:
                exit()
        elif accion == 'c':
            self.adicional = randint(self.atk1, self.atk2) * 1.4
        else:
            print("Perdiste tu turno")


espada = Arma(3)
colgante = Amuleto(5)

anillo = Amuleto(10)

putin = Jugador('Putin', 105, 16, 24)
biden = Personaje('Biden', 140, 10, 18)

putin.equipar(espada)
putin.equipar(colgante)

biden.equipar(anillo)

while putin.vivo() and biden.vivo():
    putin.atacar(biden)
    biden.atacar(putin)

    print()
    putin.status()
    biden.status()

if putin.vivo():
    print('Gano Putin')
else:
    print('Gano Biden')
