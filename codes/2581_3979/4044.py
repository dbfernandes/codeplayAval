from numpy import*

vec = array(eval(input("Digite o vetor: ")))
ent1 = 0
ent2 = 0
exit1 = 0
exit2 = 0
while (size(vec) == 5) and (vec[0] != -1):
	ent1 += vec[1]
	ent2 += vec[3]
	exit1 += vec[2]
	exit2 += vec[4]
	vec = array(eval(input("Digite o vetor: ")))		
		
print("ADM")
print("Entrada:", ent1)
print("Saida:", exit1)
print("CHAO")
print("Entrada:", ent2)
print("Saida:", exit2)
	
	