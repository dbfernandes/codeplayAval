from numpy import*
vetor = array(eval(input("matriculas do aluno: ")))
impares = 0
for i in range(size(vetor)):
	if(vetor[i]%2!=0):
		impares=impares+1
grupo2=zeros(impares,int)
n=0
for d in range(size(vetor)):
	if(vetor[d]%2!=0):
		grupo2[n]=vetor[d]
		n=n+1

print(grupo2)