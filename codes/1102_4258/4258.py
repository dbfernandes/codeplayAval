# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

from math import *

Ht = float(input("Altura total do tanque: ")) 
hn = float(input("Nivel de combustivel no tanque: ")) 
r = float(input("Raio dos bojos semiesfericos inferior e superior: ")) 

print("Entradas: ", Ht, " , ", hn, " , ", r)

if((Ht < 0 or hn < 0 or r < 0) or (Ht < hn or Ht < 2*r)):
	print("Entradas invalidas")
	
elif(hn < r):
	v = (1/3)*pi*(hn**2)*(3*r - hn)
	print("Volume: ", round(v*1000, 3), " litros")
	
elif(hn < Ht - r):
	v = ((2/3)*pi*(r**3)) + (pi*(r**2)*(hn - r))
	print("Volume: ", round(v*1000, 3), " litros")
	
elif(hn <= Ht):
	v = ((4/3)*pi*(r**3)) + (pi*(r**2)*(Ht - 2*r)) - ((1/3)*pi*((Ht - hn)**2)*(3*r - Ht + hn))
	print("Volume: ", round(v*1000, 3), " litros")
	
else:
	print("Entradas invalidas")
	