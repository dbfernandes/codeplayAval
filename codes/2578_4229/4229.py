from numpy import*
vetor=array(eval(input("Forca acumulada por cada aluno: ")))
grupo1 = 0
for i in range(size(vetor)):
	if(vetor[i]%2==0):
		grupo1=grupo1+1
grupo11=zeros(grupo1,int)
i = 0
for d in range(size(vetor)):
	if(vetor[d]%2==0):
		grupo11[i] = vetor[d]
		i = i + 1
print(grupo11)