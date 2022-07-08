from numpy import*
eusapia = array(eval(input()))
barsanulfo = array(eval(input()))

tamanho = size(eusapia)
v_eusa = 0
v_barsa = 0
cont = 0

while(cont < tamanho):
	if(eusapia[cont] == 11 and barsanulfo[cont] == 22):
		v_barsa = v_barsa + 1
	elif(eusapia[cont] == 11 and barsanulfo[cont] == 33):
		v_eusa = v_eusa + 1
	elif(eusapia[cont] == 22 and barsanulfo[cont] == 33):
		v_barsa = v_barsa + 1
	elif(eusapia[cont] == 22 and barsanulfo[cont] == 11):
		v_eusa = v_eusa + 1
	elif(eusapia[cont] == 33 and barsanulfo[cont] == 22):
		v_eusa = v_eusa + 1
	elif(eusapia[cont] == 33 and barsanulfo[cont] == 11):	
		v_barsa = v_barsa + 1
	elif(eusapia[cont] == barsanulfo[cont]):
		v_eusa = v_eusa
		v_barsa = v_barsa
	cont = cont + 1
print(tamanho)
if(v_eusa > v_barsa):
	print("EUSAPIA")
elif(v_eusa < v_barsa):
	print("BARSANULFO")
else:
	print("EMPATE")