from random import randint

# Clase 4 - Hola for

victorias_pj1 = 0
victorias_pj2 = 0

for i in range(10000):

    pj1_nombre = 'Marco Polo'
    pj1_hp = 105
    pj1_atk1 = 16
    pj1_atk2 = 24

    pj2_nombre = 'Kublai Kan'
    pj2_hp = 140
    pj2_atk1 = 10
    pj2_atk2 = 18

    while pj1_hp > 0 and pj2_hp > 0:
        daño_pj1 = randint(pj1_atk1, pj1_atk2)
        daño_pj2 = randint(pj2_atk1, pj2_atk2)

        pj1_hp = pj1_hp - daño_pj2
        pj2_hp = pj2_hp - daño_pj1

##        print(f"{pj1_nombre}: {pj1_hp}HP")
##        print(f"{pj2_nombre}: {pj2_hp}HP")
##        print()


    if pj1_hp > 0:
        victorias_pj1 += 1
    else:
        victorias_pj2 += 1


print("Victorias")
print(f"{pj1_nombre}: {victorias_pj1}")
print(f"{pj2_nombre}: {victorias_pj2}")

print(victorias_pj1/victorias_pj2)

if abs(1 - victorias_pj1/victorias_pj2) < 0.1:
    print("Están balanceados")
else:
    print("No están balanceados")
