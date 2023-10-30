from random import randint

# import/from, if/else, while, for, def, class

class Personaje:

    def __init__(self, p_nombre, p_hp, p_atk1, p_atk2):
        self.hp = p_hp
        self.hp_max = p_hp
        self.nombre = p_nombre
        self.atk_1 = p_atk1
        self.atk_2 = p_atk2
        # Cambiar p_atk por tirada de dados
        # Agregar items y la posibilidad de usarlos

    def __str__(self):
        return self.nombre

    def dmg(self):
        return randint(self.atk_1, self.atk_2)

    def status(self):
        print(f'{self.nombre} - {self.hp}/{self.hp_max}HP')

    def atacar(self, otro):
        d = self.dmg()
        otro.hp -= d
        if otro.hp < 0:
            otro.hp = 0

    def vivo(self):
        return self.hp > 0
