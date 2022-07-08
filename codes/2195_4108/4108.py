x = int(input("Digite uma data no formato DDMMAAAA: "))#data 
dia = x // 1000000
mes = (x % 1000000)//10000
ano = (x % 100000)%10000
if (ano < 1 or mes < 1 or mes > 12 or (ano % 4 != 0 and dia == 29) or (ano == 1582 and dia >= 5 and dia <=14 and mes == 10 )or (dia == 31 and (mes != 1 or mes != 3 or mes != 5 or mes != 7 or mes != 8 or mes != 10 or mes != 12))):
	 print(dia,"de",mes,"de",ano,"nao eh uma data valida")
else:
	 print(dia,"de",mes,"de",ano,"eh uma data valida")
	
	
	
