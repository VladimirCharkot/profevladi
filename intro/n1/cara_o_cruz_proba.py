from random import randint

# Clase 2 - Hola condicionales

p = randint(1,100)
vuelve_a_tirar = p < 30

apuesta = input("Ingresá cara o cruz > ")
tirada = randint(1,2)
ganaste = tirada == 1 and apuesta == 'cara' or tirada == 2 and apuesta == 'cruz'

if not(ganaste) and vuelve_a_tirar:
    apuesta = input("Perdiste. Pero te ganaste otra oportunidad. Cara o cruz? > ")
    tirada = randint(1,2)
    ganaste = tirada == 1 and apuesta == 'cara' or tirada == 2 and apuesta == 'cruz'


if ganaste:
    print('Éxito!')
else:
    print('Perdiste')
