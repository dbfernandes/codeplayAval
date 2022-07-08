from numpy import*
forca = array(eval(input("insira as forcas fracas: ")))

tamanho = 0
for i in range(size(forca)):
	if(forca[i]%2==0):
		tamanho = tamanho + 1

saida = zeros(tamanho,dtype=int)
a = 0
for i in range(size(forca)):
	if(forca[i]%2==0):
		saida[a] = saida[a] + forca[i]
		a = a + 1
print(saida)
		
