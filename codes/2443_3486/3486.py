# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input('digite o raio:'))
a = float(input('digite a altura:'))
b = float(input('digite um numero:'))
v = (4*pi*(r**3))/3
vc = ( (pi*(a**2)*((3*r) - a)) )/3
vt = v - vc
if(b == 1):
	print(round(vc, 4))
else:	
	print(round(vt,4))