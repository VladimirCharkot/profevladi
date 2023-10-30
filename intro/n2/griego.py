grec_mayus = 'ΑΒΞΔΕΦΓΗΙςΚΛΜΝΟΠΘΡΣΤΥΩΩΧΨΖΆΈΉΏΎ'
grec_minus = 'αβξδεφγηιςκλμνοπθρστυωωχψζάέήώύ'

alfa_mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÁÉÍÓÚ'
alfa_minus = 'abcdefghijklmnopqrstuvwxyzáéíóú'

def greciar(texto):
    texto = texto.replace('ñ','ni')
    nuevo = ''
    for letra in texto:
        if letra in alfa_minus:
            pos = alfa_minus.index(letra)
            nuevo += grec_minus[pos]
        elif letra in alfa_mayus:
            pos = alfa_mayus.index(letra)
            nuevo += grec_mayus[pos]
        else:
            nuevo += letra
    return nuevo

def desgreciar(texto):
    texto = texto.replace('ñ','ni')
    nuevo = ''
    for letra in texto:
        if letra in grec_minus:
            pos = grec_minus.index(letra)
            nuevo += alfa_minus[pos]
        elif letra in grec_mayus:
            pos = grec_mayus.index(letra)
            nuevo += alfa_mayus[pos]
        else:
            nuevo += letra
    return nuevo

print(greciar(input()))
