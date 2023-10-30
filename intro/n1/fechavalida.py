
def verif_fecha(dia, mes, año):
    if mes > 12:
        return False
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10  or mes == 12:
        if dia > 31:
            return False
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia > 30:
            return False
    if mes == 2:
        if dia > 28:
            return False
    return True

num_1 = int(input("Ingresá dia: "))
num_2 = int(input("Ingresá mes: "))
num_3 = int(input("Ingresá año: "))

es_valida = verif_fecha(num_1, num_2, num_3)

if es_valida:
    print("Fecha válida")
else:
    print("Fecha inválida")
