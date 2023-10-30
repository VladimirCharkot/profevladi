print('Ingresá tu nombre')
nombre = input()
print('Ingresá tu edad')
edad = input()

print('El nombre ingresado es:', nombre)
print('La edad ingresada es:', edad)

# edad es un str... lo transormamos en int
edad = int(edad)

if edad < 8:
    print(nombre + ' es niñe')
    
if edad > 7 and edad < 18:
    print(nombre + ' es adolescente')
    
if edad > 17 and edad < 40:
    print(nombre + ' es joven')
    
if edad > 39 and edad < 60:
    print(nombre + ' es adulte')
    
if edad > 59:
    print(nombre + ' es anciane')


# Instrucciones que conocemos:
#
# - Asignacion
# variable = expresión
# (expresión puede ser número, texto entre comillas, etc)
#
# - Decisión
#
# if [condición]:
#   [instrucciones]
#
# if [condición]:
#   [instrucciones si verdadero]
# else:
#   [instrucciones si falso]
#
# El espacio entre el comienzo de linea y el comienzo
# de texto se llama indentación, e indica qué cosa
# está dentro de cual otra. 


# Tipos de dato que conocemos:
# - True/False e.g. 5 < 7           (bool)
# - Números e.g. 43 + 17 * 5        (int)
# - Textos e.g. "Mi nombre es Vla"  (str)

# Funciones que conocemos:
# - str([numero]) -> Recibe un número y pone en su lugar texto
# - int([texto]) -> Recibe un texto y pone en su lugar un número
# - input() -> Pone en su lugar lo que el usuario ingrese
# - print([expresión]) -> Pone en pantalla la expresión
