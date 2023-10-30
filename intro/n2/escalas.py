cromatica = ['Do', 'Do#', 'Re', 'Re#', 'Mi', 'Fa', 'Fa#', 'Sol', 'Sol#', 'La', 'La#', 'Si']

mayor = [0,2,4,5,7,9,11]
menor = [0,2,3,5,7,8,10]

def escala(escala):
    notas = []
    for posicion in escala:
        nota = cromatica[posicion]
        notas.append(nota)
    return notas

def shift(lista, n):
    l = []
    long = len(lista)
    for i in range(long):
        l.append(lista[(n+i)%long])
    return l
