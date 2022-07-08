a = int(input("Limite inferior do intervalo: "))
b = int(input("Limite superiro do intervalo: "))

for i in range(a, b+1):
	if (i%6 == 0):
		print(i)