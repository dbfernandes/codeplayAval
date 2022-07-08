from numpy import*

vetor = array(eval(input("Forca acumulada: ")))

par = 0

for i in range(size(vetor)):
	if(vetor[i]%2==0):
		par = par + 1
		
cont = zeros(par,dtype=int)
p = 0

for m in range(size(vetor)):
	if(vetor[m]%2==0):
		cont[p] = cont[p] + vetor[m]
		p = p + 1
		
print(cont)