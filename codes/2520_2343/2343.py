from math import *
n = int(input())
i = 1
soma = 0
while(i <= n):
	soma = soma + 6/(i**2)
	i = i + 1
	
pi = sqrt(soma)
print(round(pi,6))