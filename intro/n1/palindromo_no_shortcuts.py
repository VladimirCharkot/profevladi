# 4.1, 4.7, 4.8

capi1 = 'neuquen'
capi2 = 'ana'
capi3 = 'anitalavalatina'


def es_capicua(texto):
    
    l = len(texto)
    mitad = int(l/2)
    
    for i in range(mitad):
        if texto[i] != texto[l-1-i]:
            return False

    return True


if es_capicua('camello'):
    print('Hay un problema')

if not(es_capicua(capi3)):
    print('Hay un problema')
