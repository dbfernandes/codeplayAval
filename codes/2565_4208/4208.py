from numpy import*

vet1 = array(eval(input("media: ")))
vet2 = array(eval(input("presenca: ")))
ch = int(input("carga horaria: "))
vet = zeros(3, dtype=int)
for i in range(size(vet1)):
	if vet1[i] > 5 and vet2[i] >= ch*75/100:
		vet[0] = vet[0] + 1
	elif vet1[i] < 5 and vet2[i] >= ch*75/100:
		vet[1] = vet[1] + 1
	elif vet1[i] < ch*75/100:
		vet[2] = vet[2] + 1
print(vet)
			