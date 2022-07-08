from numpy import *
from numpy.linalg import *
ordem = array(eval(input("Digite a ordem da matriz: ")))

mat = zeros((ordem, ordem))
for i in range(ordem):
	for j in range(ordem):
		valor = int(input("Digite a ordem da matriz: "))
		mat[i,j] = valor
		
principal = 0
for i in range(ordem):
	for j in range(ordem):
		if(i == j):
			principal = principal + mat[i,j]

aux = zeros((ordem, 1))
for i in range(ordem//2):
	aux[:,0] = mat[:,i]
	mat[:,i] = mat[:, -1-i]
	mat[:, -1-i] = aux[:,0]

secundaria = 0
for i in range(ordem):
	for j in range(ordem):
		if(i == j):
			secundaria = secundaria + mat[i,j]
dif = int(principal - secundaria)
print(dif)		