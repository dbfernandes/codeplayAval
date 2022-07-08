from numpy import*

vec_tam = array(eval(input("digite o diametro(cm) das batatas: ")))

tipo_a = 0
tipo_b = 0
tipo_c = 0

i = 0
while (i < size(vec_tam)):
	if (vec_tam[i] >= 10):
		tipo_a += 1
	elif (vec_tam[i] >= 5) and (vec_tam[i] < 10):
		tipo_b += 1
	elif (vec_tam[i] < 5):
		tipo_c += 1
	i += 1
print(tipo_a)
print(tipo_b)
print(tipo_c)