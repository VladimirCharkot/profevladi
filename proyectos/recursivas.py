# factorial(n) -> n * factorial(n - 1)
# factorial(5) -> 5 * factorial(4)
# factorial(5) -> 5 * 4 * factorial(3) 
# factorial(5) -> 5 * 4 * 3 * factorial(2) 

def factorial(n):
    if n == 1:
        return 1
    print(f"Devolviendo {n} * factorial({n - 1})")
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    r1 = fibonacci(n-1)
    r2 = fibonacci(n-2)
    return r1 + r2

def otre(jugadore):
    if jugadore == 'Primero':
        return 'Segundo'
    return 'Primero'

def uno_o_dos(juega, num):
    print(f"Juega {juega} con {num}")
    if num == 19 or num == 20:
        return juega
    c1 = uno_o_dos(otre(juega), num + 1)
    print(f"Si suma 1 gana {c1}")
    c2 = uno_o_dos(otre(juega), num + 2)
    print(f"Si suma 2 gana {c2}")
    if c1 == juega:
        return c1
    else: 
        return c2

def other(player):
    if player == 'First':
        return 'Second'
    return 'First'

def gos(player, n):
    if n == 1:
        return other(player)
    if n == 2 or n == 3 or n == 5:
        return player
    c1, c2, c3 = None, None, None
    c1 = gos(other(player), n - 2)
    if n >= 3:
        c2 = gos(other(player), n - 3)
    if n >= 5:
        c3 = gos(other(player), n - 5)
    if player in [c1, c2, c3]:
        return player
    else:
        return other(player)
    
print(gos('First', 6))