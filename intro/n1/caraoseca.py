from random import random

def caraosello(nombre_cara, nombre_sello, p):
    cara = random() <= p

    if cara:
        return nombre_cara
    else:
        return nombre_sello
