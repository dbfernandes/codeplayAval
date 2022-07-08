from math import*

n = int(input("Digite um numero: "))

soma = 0
i = 1

while(i<=n) and (n!=0):
	soma = soma + 1/(i**2)
	i = i + 1

pi = sqrt(soma*6)
print(round(pi,6))