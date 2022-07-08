from math import *
from numpy import *

x = eval(input("Angulo: "))
k = int(input("Numero inteiro: "))
h = 0

for i in range(0,k):
	p = (((-1)**i)*(x**(2*i)))/(factorial(2*i))
	h = h + p
print(round(h, 11))

