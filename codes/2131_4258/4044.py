from math import*

x = eval(input("Angulo em radianos: "))
n = int(input("Quantidade de termos: "))

soma = 0
for i in range(n):
	soma += ((x**(2*i))/(factorial(2*i)))*((-1)**(i))
print(round(soma, 11))