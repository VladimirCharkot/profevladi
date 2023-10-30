a = int(input("Ingresa año actual: "))
b = int(input("Ingresa mes actual: "))
c = int(input("Ingresa dia actual: "))

#if b > 0 and b < 13 and a > 0:

if b < 0 or b > 13 or a < 0:
    print("fecha incorrecta")
        
else:

    if b == 2:
        if c > 0 and c < 29:
            print("Fecha correcta")
        else:
            print("fecha incorrecta")
            
    elif b == 1 or b == 3 or b==5 or b==6 or b==7 or b==8 or b==10 or b==12:
        if c > 0 and c < 32:
            print("Fecha correcta")
    else: 
        if c > 0 and c < 31:
            print("fecha correcta")
        else:
            print("fecha incorrecta")
    
