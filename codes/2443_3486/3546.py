# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

r = float(input("raio: "))
x = float(input("altura: "))
opcao = int(input("opcao: "))

V_esfera = (4*pi*r**3)/3

V_ar = (pi*x**2*(3*r - x))/3

V_combust = V_esfera - V_ar

if(opcao == 1):
	print(round(V_ar, 4))
else:
	print(round(V_combust, 4))