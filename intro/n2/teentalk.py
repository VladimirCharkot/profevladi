import random

def teentalk(texto, probabilidad = 0.5):
  nuevo = ''
  for letra in texto:
    if random.random() < probabilidad:
      nuevo += letra.upper()
    else:
      nuevo += letra.lower()
  return nuevo

# Duck typing --> Tipado "Pato"
# "Un objeto es un pato si dice quack"
# Un objeto es lo que espero que sea
# si hace lo que espero que haga

sed_verdadera = '''
Se muy bien que has oido hablar de mi
Y hoy nos vemos aqui
Pero la paz
En mi nunca la encontrarás
Si no es en vos
En mi nunca la encontrarás
Por tu living o fuera de alli no estás
Pero hay otro que está
Y yo no soy
Yo solo te hablo desde aquí
Él debe ser la musica que nunca hiciste
Viste la piel
Creiste en todo lo que te di
Nada salió de vos
Ah mira el fuego
Las luces que saltan a lo lejos
No esperan que vayas a apagarlas
Jamás...'''

print(teentalk(sed_verdadera))
