# Contamos la cantidad de ocurrencias de cada número con tres dados de seis

ocurrencias = {}

for i in range(6):
    for j in range(6):
        for k in range(6):
            v = i + j + k + 3
            print(f'Evaluando {i+1} + {j+1} + {k+1} = {v}')
            if v in ocurrencias:
                ocurrencias[v] += 1
            else:
                ocurrencias[v] = 1

print(ocurrencias)
