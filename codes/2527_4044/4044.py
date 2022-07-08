n = int(input("Digite um numero: "))

i = 1
soma = 0

while (i < n):
    if (n%i == 0):
        print(i)          
        soma += i
    i += 1
    
if (soma == n):
    print("PERFEITO")
else:
    print("NAO PERFEITO")    