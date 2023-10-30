import matplotlib.pyplot as plt

plt.xkcd()

edades = [34,56,21,74,23,62,36,89,65,11,23,8,34,98,24,36]
bins = [10*n for n in range(9)]
#plt.hist(edades)

x1 = [1,3,5,7,9]
y1 = [5,7,4,6,2]
#plt.bar(x1, y1, label='Bars1', color = 'r')

x1 = [0,2,4,6,8]
y1 = [8,9,2,7,9]
#plt.bar(x1, y1, label='Bars2', color = 'c')

plt.scatter(x1, y1, color='k', marker='*', s=1000)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Grafico boh\nWololo')

plt.show()
