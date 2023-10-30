# Vamos a armar mochilas de viaje para un equipo de personas.
# Preguntar al usuario cuántas mudas de ropa, cuántos tapers y
# cuántos carretes de hilo debería llevar cada mochila y
# luego preguntar cuántas personas van al viaje.
# Responder qué cantidad de cada cosa necesitamos comprar,
# y cuántos objetos en total tenemos.
# Puntos extra: Preguntar también los precios de cada cosa
# y calcular un presupuesto.

# Clase 1 - Instrucciones y expresiones

ropas = int(input("Cuántas mudas de ropa por mochila?"))
tuppers = int(input("Cuántos tuppers por mochila?"))
hilos = int(input("Cuántos carretes de hilo por mochila?"))

personas = int(input("Cuántas personas van al viaje?"))

print("Necesitamos comprar...")
print(ropas * personas, "mudas de ropa")
print(tuppers * personas, "tuppers")
print(hilos * personas, "carretes de hilo")

print("Son", (ropas + tuppers + hilos) * personas, "en total")

precio_ropa = float(input("Cuánto sale una muda de ropa?"))
precio_tupper = float(input("Cuánto sale un tupper?"))
precio_hilo = float(input("Cuánto sale un carrete de hilo?"))

precio_por_persona = ropas * precio_ropa \
                     + tuppers * precio_tupper \
                     + hilos * precio_hilo

presupuesto_total = precio_por_persona * personas

print("El presupuesto total es", presupuesto_total)
