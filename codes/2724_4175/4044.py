n1 = int(input("1. Digite o primeiro numero: "))
n2 = int(input("2. Digite o segundo numero: "))
n3 = int(input("3. Digite o terceiro numero: "))

menor = 0
maior = 0
inter = 0

# Código para descobrir o menor número

if (n1 < n2):
	if (n1 < n3):
	   menor = n1
if (n2 < n1):
	if (n2 < n3):
		menor = n2
if (n3 < n1):
	if (n3 < n2):
		menor = n3
		
# Código para descobrir o maior número
		
if (n1 > n2):
	if (n1 > n3):
		maior = n1
if (n2 > n1):
	if (n2 > n3):
		maior = n2
if (n3 > n1):
	if (n3 > n2):
		maior = n3

print((n1 + n2 + n3) - (menor + maior))
