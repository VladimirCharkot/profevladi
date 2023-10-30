texto = 'lspe$ferhe$gsqs$erher'

for i in range(26):
    encriptado = ''
    for letra in texto:
        encriptado = encriptado + chr(ord(letra) - i)

    print(str(i) +': ' + encriptado)


for i in range(26):
    encriptado = ''
    for letra in texto:
        encriptado = encriptado + chr(ord(letra) + i)

    print(str(i) +': ' + encriptado)

#texto = input()

#print()
#encriptado = ''
#for letra in texto:
#    encriptado = encriptado + chr(ord(letra) + 4)

#print(encriptado)
