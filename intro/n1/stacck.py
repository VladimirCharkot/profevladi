# Clase 7 - Práctica

def uno(c, p):
  u = 0
  for j in p:
    if c == j:
      u += 1
  return u


def dos(l):
  c = True
  for y in l:
    if c:
      print(' ' * y, end='')
    else:
      print('#' * y, end='')
    c = not(c)
  print()


def tres():
  global o
  if o % 2 == 0:
    o = o / 2
  else:
    o = o * 3 + 1
  return o == 1


def bla(t):
  l = len(t)
  if l < 2:
    return True
  else:
    return t[0] == t[l-1] and bla(t[1:l-1])

