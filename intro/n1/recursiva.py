def recursiva(n):
    print(f'hola {n}')
    if n == 100: 
            return n
    else:
            return n + recursiva(n + 3)

def otre(j):
  if j == 'Primero':
    return 'Segundo'
  return 'Primero'

def uno_o_dos(juega, num):
  print(f"Juega {juega} con {num}")
  if num == 19 or num == 20:
    return juega
  c1 = uno_o_dos(otre(juega), num + 1)
  print(f"Si suma 1 gana {c1}")
  c2 = uno_o_dos(otre(juega), num + 1)
  print(f"Si suma 2 gana {c2}")
  if c1 == juega:
    return c1
  else:
    return c2
  
# r = uno_o_dos('Primero', 16)
# print(r)


def posibles(texto):
  if len(texto) == 1:
    return [texto]
  else: 
    ps = []
    for i in range(1, len(texto) - 1):
      ps.extend([texto[:i]] + posibles(texto[i:]))
    return ps
    
print(posibles('abcd'))
# [
  # ['a', 'b', 'c', 'd'],
  # ['a', 'b', 'cd'],
  # ['a', 'bc', 'd'],
  # ['a', 'bcd'],
  # ['ab', 'c', 'd'],
  # ['ab', 'cd'],
  # ['abc', 'd'],
  # ['abcd']
# ]
