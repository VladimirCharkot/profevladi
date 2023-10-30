
# Calcular el vuelto
# Ir recorriendo los billetes del más grande al más chico
# e ir descontando del vuelto hasta llegar a cero

# Existen $500, $100, $50, $20, $10, $5 y $1

def dar_vuelto(precio, recibido):

    if precio > recibido:
        print("Error, dinero insuficiente")
        return "error"

    vuelto = []
    a_devolver = recibido - precio

    # A la variable a_devolver le vamos a 
    # ir descontando lo que agreguemos a vuelto
    while a_devolver > 0:
        
        if a_devolver >= 500:
            vuelto += [500]
            a_devolver -= 500
            continue
        
        if a_devolver >= 100:
            vuelto += [100]
            a_devolver -= 100
            continue

        if a_devolver >= 50:
            vuelto += [50]
            a_devolver -= 50
            continue
                    
        if a_devolver >= 20:
            vuelto += [20]
            a_devolver -= 20
            continue
                    
        if a_devolver >= 10:
            vuelto += [10]
            a_devolver -= 10
            continue
                    
        if a_devolver >= 5:
            vuelto += [5]
            a_devolver -= 5
            continue

        if a_devolver >= 1:
            vuelto += [1]
            a_devolver -= 1
            continue
        
    return vuelto


# dar_vuelto(317, 500)
# [100, 50, 20, 10, 1, 1, 1]

# $831
# le puedo dar $500?
#   entonces agrego 500 a la lista, y le descuento 500 a_devolver

valor_texto = input("Ingresá el precio: ")
valor = int(valor_texto)

pago_texto = input("Ingresá el pago del cliente: ")
pago = int(pago_texto)

billetes = dar_vuelto(valor, pago)

if billetes != "error":
    print("Tenemos que dar de vuelto:")
    print(billetes)

