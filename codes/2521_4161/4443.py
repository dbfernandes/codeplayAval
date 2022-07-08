from math import *
n = int(input("digite um numero inteiro positivo: "))

i = 2
soma = 1+1/3
d = 3
t = 2
while(t <= n):
	num = factorial(t)
	d = d*(2*i+1)
	pi = num/d
	soma = soma + pi
	i = i +1
	t = t+1
	
soma = 2*soma
print(round(soma, 10))