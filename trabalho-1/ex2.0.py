import matplotlib.pyplot as plt 
x = []
y = []
count = 0
while True:
    i = int(input('Digite os valores de X: '))
    x.append(i)
    count += 1
    if count >= 3:
        break
    
for i in x:
    a = 9*i + 9*i - 9
    y.append(a)

print(
    f"Valores de Y em relação a expressão f(x)= 9x+9x-9:\n"
    f"{y[0]}\n"
    f"{y[1]}\n"
    f"{y[2]}"
) 
plt.scatter(x,y, label="Pares Ordenados (X,Y)")
plt.plot(x,y,"-r", label="Reta da função")
plt.legend(loc="upper left")
plt.title("Gráfico da função f(x)= 9x + 9x -9 (RU:3879999)")
plt.xlabel("Eixo das abcissas (X)")
plt.ylabel("Eixo das ordenadas (Y)")
plt.show()