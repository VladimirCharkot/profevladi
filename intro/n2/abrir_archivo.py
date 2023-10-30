archivo = open('castellano.txt', encoding='utf8')
castellano = archivo.read()
archivo.close()
dicc = castellano.split('\n')
