# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *
r=float(input("Raio do tanque: "))
x=float(input("Altura da coluna de ar na parte superior do tanque: "))
volume = (4*pi*(r**3))/3
volume_ar= (pi*(x**2)*(3*r-x))/3
opcao=input("Opcao desejada (1/2): ")
if(opcao == "1"):
	print(round(volume_ar, 4))
if(opcao == "2"):
	print(round((volume - volume_ar), 4))