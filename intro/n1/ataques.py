import random

personaje_1_hp = 900
personaje_1_atk = 50

personaje_2_hp = 400
personaje_2_atk = 90

while personaje_1_hp > 0 and personaje_2_hp > 0:
    
    danio_personaje_1 = random.randrange(1, personaje_1_atk)
    personaje_2_hp = personaje_2_hp - danio_personaje_1

    danio_personaje_2 = random.randrange(1, personaje_2_atk)
    personaje_1_hp = personaje_1_hp - danio_personaje_2

    print('Personaje 1 hizo ' + str(danio_personaje_1) + ' puntos de daño')
    print('Personaje 2 hizo ' + str(danio_personaje_2) + ' puntos de daño')
    print('Personaje 1 -> ' + str(personaje_1_hp) + ' HP')
    print('Personaje 2 -> ' + str(personaje_2_hp) + ' HP')
    print()
