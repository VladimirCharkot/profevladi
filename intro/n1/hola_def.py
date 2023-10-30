#2- Escribir un script que juegue piedra papel o tijera contra la máquina \
#hasta que gane ella. Luego printear la cantidad de veces que ganó usuarie.

from random import randint


# Jugar PPT
# Preguntar
# while Continuar:
#   Jugar PPT
#   Preguntar

def ppt():
    opc = input ("Piedra, papel o tijera? ")
    compu = randint (1, 3)
    if compu == 1:
        compu = "piedra"
    if compu == 2:
        compu = "papel"
    if compu == 3:
        compu = "tijera"
    print ()
    print ("La compu sacó: " + compu)
    print ()
    if opc == compu:
        print ("EMPATE") 
    if opc == ("piedra") and compu == ("papel"):
        print ("PERDISTE")
    if opc == ("piedra") and compu == ("tijera"):
        print ("GANASTE")
    if opc == ("papel") and compu == ("piedra"):
        print ("GANASTE")
    if opc == ("papel") and compu == ("tijera"):
        print ("PERDISTE")
    if opc == ("tijera") and compu == ("piedra"):
        print ("PERDISTE")
    if opc == ("tijera") and compu == ("papel"):
        print ("GANASTE")


ppt()
resp = input("Continuar? ")
    
while resp == "si":
    ppt()
    resp = input("Continuar? ")

