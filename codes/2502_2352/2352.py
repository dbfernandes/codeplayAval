n = int(input("Digite o valor de n: "))

c = 0
a = 0

while(c < n):
	a = a + (12) ** 0.5 * (-1) ** (c) * (1 / ((2 * c + 1) * (3) ** c))
	c = c + 1
	
print(round(a ,8))