from time import sleep

# Clase 5 - Funciones

textos = [
    'Hola humano',
    'veo que te ha sorprendido que te hable',
    'No te preocupes, tan solo quiero hacerte daño'
]

# No devuelve nada
def progresivo(texto):
    for letra in texto:
            print(letra, end='')
            sleep(0.01)

# Devuelve respuesta
def preguntar(pregunta):
    progresivo(pregunta)
    print()
    respuesta = input("> ")
    return respuesta

# Devuelve txt invertido
def invertir(txt):
    nuevo = ''
    for letra in txt:
        nuevo = letra + nuevo
    return nuevo

for texto in textos:
    progresivo(texto)
    sleep(1)
    print()

r = preguntar("Estás de acuerdo en que esto es maravilloso?")

if r in 'SiSísisíSÍSIaham':
    progresivo('Estamos de acuerdo')
else:
    progresivo('Preparate para morir')
