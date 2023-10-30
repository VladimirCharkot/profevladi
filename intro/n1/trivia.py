puntaje = 0

def pregunta(texto_pregunta, respuesta_correcta):
    print(texto_pregunta)
    r = input()

    global puntaje
    if r == respuesta_correcta:
        puntaje = puntaje + 1 
        print('Correcto')
    else:
        print('Incorrecto')

pregunta('Cuántas patas tiene una rana', '4')
pregunta('Cuántos mates te ceba un termo', '20')

print('Tu puntaje es', puntaje)
