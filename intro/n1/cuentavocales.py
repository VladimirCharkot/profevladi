

def vocal_protagonista(texto):
    cantidad_a = 0
    cantidad_e = 0
    cantidad_i = 0
    cantidad_o = 0
    cantidad_u = 0

    for letra in texto:
        if letra == 'a':
            cantidad_a += 1
            
        if letra == 'e':
            cantidad_e += 1
            
        if letra == 'i':
            cantidad_i += 1
            
        if letra == 'o':
            cantidad_o += 1
            
        if letra == 'u':
            cantidad_u += 1

    ganadora = max(cantidad_a, cantidad_e, cantidad_i, cantidad_o, cantidad_u)

    if cantidad_a == ganadora:
        return 'a'
    if cantidad_e == ganadora:
        return 'e'
    if cantidad_i == ganadora:
        return 'i'
    if cantidad_o == ganadora:
        return 'o'
    if cantidad_u == ganadora:
        return 'u'
    

def compactar(num_int):
    suma = 10
    
    while suma > 9:
        num = str(num_int)
        suma = 0
        for digito in num:
            n = int(digito)
            suma = suma + n
        num_int = suma
        
    return suma
    

    
