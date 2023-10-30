frutas_dulces = ['banana', 'cerezas', 'pera']
frutas_acidas = ['naranja', 'frutilla', 'limon']

print('Ingresame una fruta:')
fruta = input()

if fruta in frutas_dulces:
    print('Es dulce!')
else:
    if fruta in frutas_acidas:
        print('Es ácida')
    else:
        print('No la conozco ._.')
