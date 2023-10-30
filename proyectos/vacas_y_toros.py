from random import choices

# TP

simbolos = '0123456789'
digitos = 4

# clave = []
# for __ in range(4):
#     clave += random.choice(simbolos)

def lista_a_string(lis):
    s = ''
    for car in lis:
        s += car
    return s

clave = lista_a_string(choices(simbolos, k=digitos))

oportunidades = 7
intentos = 0
acertado = False
quedan_intentos = True
while not acertado and quedan_intentos:
    vacas = []
    toros = []
    resto = []
    print("Cuál es el número?")
    respuesta = input("> ")
    if respuesta == 'x': break
    for apuesta, simbolo in zip(respuesta, clave):
        if apuesta == simbolo:
            vacas += apuesta
        else:
            resto += apuesta
    for apuesta in resto:
        if apuesta in clave:
            toros += [apuesta]
    # print("v", vacas)
    # print("r", resto)
    # print("t", toros)
    anuncio = ""
    # Python interpreta el 0 como False y los demás números como True
    if vacas and len(vacas) < digitos:
        anuncio += f"Tenés {len(vacas)} vacas"
    if toros and vacas:
        anuncio += f" y {len(toros)} toros"
    if toros and not vacas:
        anuncio += f"Tenés {len(toros)} toros"
    if not vacas and not toros:
        anuncio += f"Ni vacas ni toros!"
    print(anuncio)
    acertado = len(vacas) == digitos
    # quedan_intentos = intentos < oportunidades
    quedan_intentos = True
    intentos += 1

if acertado:
    print(f"Ganaste en {intentos} intentos!")
else:
    print(f"Perdiste. Era {clave}")
