
def cuento_chino(patas, cabezas):
    
    for i in range(cabezas):
        cant_conejos = i + 1
        cant_gallinas = 35 - cant_conejos
        patas_ahora = cant_conejos * 4 + cant_gallinas * 2
        
        if patas_ahora == patas:
            #print("Entre " + str(cant_conejos) + " conejos y " + str(cant_gallinas) + " gallinas hacen " + str(patas) + " patas")
            print(f"{patas} patas se hacen entre {cant_conejos} conejos y {cant_gallinas} gallinas")

def saludar(nombre):
    #print(f'Hola cómo va {nombre}')
    return f'Hola cómo va {nombre}'

def cuadrado(numero):
    return numero**2




    
cuento_chino()
