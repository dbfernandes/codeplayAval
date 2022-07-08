from numpy import *

vet = array(eval(input()))
adm_entrada = 0
adm_saida = 0
chao_entrada = 0
chao_saida = 0

while(size(vet) == 5):
	adm_entrada += vet[1]
	adm_saida += vet[2]
	chao_entrada += vet[3]
	chao_saida += vet[4]
	
	vet = array(eval(input()))

print('ADM')
print('Entrada: ' + str(adm_entrada))
print('Saida: ' + str(adm_saida))
print('CHAO')
print('Entrada: ' + str(chao_entrada))
print('Saida: ' + str(chao_saida))