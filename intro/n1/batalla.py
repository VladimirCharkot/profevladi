from random import randint
from time import sleep

pj1_hp = 120
pj1_atk_1 = 4
pj1_atk_2 = 12
pj1_nombre = 'Rigoberto'

pj2_hp = 180
pj2_atk_1 = 2
pj2_atk_2 = 8
pj2_nombre = 'Anastasia'

while pj1_hp > 0 and pj2_hp > 0:
    dmg_1 = randint(pj1_atk_1, pj1_atk_2)
    dmg_2 = randint(pj2_atk_1, pj2_atk_2)
    pj1_hp -= dmg_2
    pj2_hp -= dmg_1

    if pj1_hp < 0:
        pj1_hp = 0

    if pj2_hp < 0:
        pj2_hp = 0

    print(f'{pj1_nombre}: {pj1_hp}HP')
    print(f'{pj2_nombre}: {pj2_hp}HP')
    print()
    sleep(0.1)

if pj1_hp > 0:
    print(f'Ganó {pj1_nombre}')
else:
    print(f'Ganó {pj2_nombre}')
