frase = input('Ingresá una frase > ')
desp = int(input('Cuantos caracteres queres desplazar?? '))
nueva_frase = ''

for letra in frase:
    numero = ord(letra)
    nuevo_num = numero + desp 
    nueva_letra = chr(nuevo_num)
    nueva_frase += nueva_letra

print(nueva_frase)