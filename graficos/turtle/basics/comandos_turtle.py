from turtle import *

# La longitud del paso está hardcodeada
# Convertirla en una variable al principio del script pls

comandos = input("Ingresá una secuencia de letras wasd: ")
n = 0

while n < len(comandos):
    comando = comandos[n]
    if not(comando in 'wasd'):
        print(f'No entiendo este comando: {comando}')
    if comando == 'd':
        seth(0)
        forward(50)
    if comando == 'w':
        seth(90)
        forward(50)
    if comando == 'a':
        seth(180)
        forward(50)
    if comando == 's':
        seth(270)
        forward(50)
    n += 1
