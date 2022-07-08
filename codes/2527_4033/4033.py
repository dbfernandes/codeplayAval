num=int(input("Digite um numero inteiro positivo: "))

i=1
soma=0

while(i<num):
	if(num%i==0):
		print(i)
		soma=soma+i
	i=i+1

if(soma==num and num>0):
	print("PERFEITO")
elif(soma!=num and num>0):
		print("NAO PERFEITO")

