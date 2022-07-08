# Ao testar sua solução, não se limite ao caso de exemplo.
n = float(input("numero de horas extras: "))
f = float(input("numeros de horas faltosas: "))
m = float(500)
p = float(100)
h = n - ((1/4)*f)
print(n, "extras e", f, "de falta")
if (n>=0 and f>=0):
	if(0<= h <= 400):
		print("R$", round(p, 2))
	else:
		print("R$", round(m, 2))