from numpy import*

coef = array(eval(input("coeficientes de uma funcao polinomial: ")))

eq = ""
i = size(coef) - 1
j = 0
while (i >= 0):
	if (i >= 2):
		eq = eq + str(coef[j]) + "x^%d" %(i) + " + "
	elif (i == 1):
			eq = eq + str(coef[j]) + "x" + " + "
	elif (i == 0):
			eq = eq + str(coef[j])
		
	i -= 1
	j += 1
print(eq)