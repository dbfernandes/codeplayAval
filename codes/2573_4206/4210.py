from numpy import*
peso = array(eval(input("peso: ")))
altura = array(eval(input("altura: ")))
imc = zeros(size(peso),dtype=float)

for i in range(size(peso)):
	imc[i] = round(peso[i]/altura[i]**2,2)
	
print(imc)
j = max(imc)
print("O MAIOR IMC DA TURMA EH:",j)
if(j<17):
	print("MUITO ABAIXO DO PESO")
elif(j>17 and j<18.49):
	print("ABAIXO DO PESO")
elif(j>18.5 and j<24.99):
	print("PESO NORMAL")
elif(j>25 and j<29.99):
	print("ACIMA DO PESO")
elif(j>30 and j<34.99):
	print("OBESIDADE")
elif(j>35 and j<39.99):
	print("OBESIDADE SEVERA")
elif(j>40):
	print("OBESIDADE MORBIDA")