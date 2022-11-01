#Variaveis pré definidas
x1=5
x2=7
x3=9

y1 = 9*x1 + 9*x1 - 9
y2= 9*x2 + 9*x2 - 9
y3= 9*x3 + 9*x3 - 9 

# VALORES A SEREM PLOTADOS

import matplotlib.pyplot as plt

x = [x1,x2,x3]
y = [y1,y2,y3]

print(f'Y1 = 9*{x1} + 9*{x1} - 9 = {y1} \nY2 = 9*{x2} + 9*{x2} - 9 = {y2} \nY3 = 9*{x3} + 9*{x3} - 9 = {y3}')

plt.scatter(x,y, label="Pares Ordenados (X,Y)")
plt.plot(x,y, "-r", label="Reta da função")
plt.legend(loc="upper left")
plt.title("Gráfico da função Y = 9x + 9x - 9 (RU:3879999)")
plt.xlabel("Eixo das abcissas (X)")
plt.ylabel("Eixo das ordenadas (Y)")
plt.show()
