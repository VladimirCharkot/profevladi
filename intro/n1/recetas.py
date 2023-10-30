# Clase 2 - Hola condicionales

print('Veamos qué se puede preparar con lo que tenés en la cocina...')
papa = input('Tenés papa? [s/n] ') == 's'
zanahoria = input('Tenés zanahoria? [s/n] ') == 's'
zapallo = input('Tenés zapallo? [s/n] ') == 's'
cebolla = input('Tenés cebolla? [s/n] ') == 's'
acelga = input('Tenés acelga? [s/n] ') == 's'
queso = input('Tenés queso? [s/n] ') == 's'
huevo = input('Tenés huevo? [s/n] ') == 's'
lechuga = input('Tenés lechuga? [s/n] ') == 's'
tomate = input('Tenés tomate? [s/n] ') == 's'
zanahoria = input('Tenés zanahoria? [s/n] ') == 's'
repollo = input('Tenés repollo? [s/n] ') == 's'
rucula = input('Tenés rúcula? [s/n] ') == 's'
harina = input('Tenés harina? [s/n] ') == 's'
polvo = input('Tenés polvo de hornear? [s/n] ') == 's'
aceite = input('Tenés aceite? [s/n] ') == 's'
ajo = input('Tenés ajo? [s/n] ') == 's'
garbanzo = input('Tenés garbanzo? [s/n] ') == 's'
perejil = input('Tenés perejil? [s/n] ') == 's'

print("Podés preparar...")

if papa and huevo:
    print("...tortilla")
    if zanahoria and zapallo:
        print("...verduras hervidas: papa, huevo, zanahoria y zapallo")
    elif zanahoria:
        print("...verduras hervidas: papa, huevo y zanahoria")
    elif zapallo:
        print("...verduras hervidas: papa, huevo y zapallo")
    else:
        print("...ensalada de papa y huevo")

if ajo and garbanzo and cebolla and perejil:
    print("...falafel")

if lechuga and tomate:
    if cebolla:
        print("...ensalada de lechuga, tomate y cebolla")
    else:
        print("...ensalda de lechuga y tomate")

if rucula and tomate:
    if ajo:
        print("...ensalada de rúcula, tomate y ajo")
    else:
        print("...ensalada de rúcula y tomate")

if zanahoria and repollo:
    print("...una ensalada de zanahoria y repollo")

if harina and polvo and aceite and queso:
    if cebolla:
        print("... tarta de cebolla y queso")
    if acelga and huevo:
        print("... una pascualina")
    if repollo:
        print("... una tarta de repollo")
