from functools import reduce
from random import randint
 
def tirada(n):
    return [randint(1,6) for i in range(5)]
 
def es_generala(tirada):
    es = True
    for i in range(len(tirada) - 1):
        es = es and tirada[i] == tirada[i + 1]
    return es
 
    #return reduce(lambda a, b: a == b, tirada)
 
def es_escalera(tirada):
    es = True
    for i in range(len(tirada) - 1):
        es = es and tirada[i] == tirada[i + 1] - 1
    return es
 
    #return reduce(lambda a, b: a and a == b - 1, tirada)
 
def es_foul(tirada):
    if not len(set(tirada)) == 2: return False
    a, b = [tirada.count(k) for k in set(tirada)]
    return (a == 2 and b == 3) or (a == 3 and b == 2)
 
def es_poker(tirada):
    return 4 in [tirada.count(k) for k in set(tirada)]
 
notario = {}
 
def puntaje(tirada):
 
    if es_generala(tirada):
        return 'generala', 50
    if es_poker(tirada):
        return 'poker', 40
    if es_foul(tirada):
        return 'foul', 30
    if es_escalera(tirada):
        return 'escalera', 20
 
    posibles = [(n, n * tirada.count(n)) for n in set(tirada) if n not in notario]
    if not(posibles):
        return 'nada', 0
 
    posibles.sort(key=lambda par: -par[1])  # Por puntos, descendente
 
    return posibles[0]    # (num, cant)
 
 
def tiene_juego(tirada):    
	return es_generala(tirada) or es_escalera(tirada) or \
           es_foul(tirada) or es_poker(tirada)
 
 
def buscar(buscada):   
	t = tirada(5)
	r, p = puntaje(t)
	c = 1
	while r != buscada:
		t = tirada(5)        
		r, p = puntaje(t)
		c += 1
	return c
 
 
def gameloop():
 
	ensayos = 10  
 
	intentos_escalera = 0
	for i in range(ensayos):
		b = buscar('escalera')
		intentos_escalera += b
		print('Escalera en', b, 'intentos')
	print('=' * 80)
 
	intentos_generala = 0
	for i in range(ensayos):
		b = buscar('generala')
		intentos_generala += b
		print('Generala en', b, 'intentos')
 
	print('=' * 80)
	print('Promedio escalera', intentos_escalera / ensayos)
	print('Promedio generala', intentos_generala / ensayos)
 
 
 
gameloop()