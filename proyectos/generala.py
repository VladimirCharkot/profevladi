from random import randint

# Clase 5

def dado(n):
    return randint(1,n)

def cinco_dados(n):
    dados = []
    for i in range(5):
        dados = dados + [dado(n)]
    return dados

def dados(cant, caras):
    dados = []
    for i in range(cant):
        dados = dados + [dado(caras)]
    return dados



def es_generala(tirada):
    if tirada[0] == tirada[1] == tirada[2] ==tirada[3] == tirada[4]:
        return True
    else:
        return False


suma = 0
ensayos = 10000

for n in range(ensayos):
    terminar = False
    cantidad = 0

    while not terminar:
        cantidad = cantidad + 1
        ds = dados(5,6)
        terminar = es_generala(ds)

    suma = suma + cantidad

print("Para que tirando cinco dados salga generala de una, en promedio son necesarios", suma/ensayos, "ensayos")
