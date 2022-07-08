from numpy import*
from numpy.linalg import*
#matriz
mat=array(eval(input("")))
#dia da semana
sem=shape(mat)[1]
#vetor contador
vet=zeros(sem,dtype=int)

for j in range(sem):
	vet[j]=vet[j]+sum(mat[:,j])
#print(vet)
#dia da semana que mais trabalha
if(vet[0]==max(vet)):
	print(1)
if(vet[1]==max(vet)):
	print(2)
elif(vet[2]==max(vet)):
	print(3)
elif(vet[3]==max(vet)):
	print(4)
elif(vet[4]==max(vet)):
	print(5)
elif(vet[5]==max(vet)):
	print(6)
else:
	print(7)

