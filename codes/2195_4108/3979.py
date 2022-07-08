data = int(input())

ano = data % 10000
mes = (data % 1000000)//10000
dia = data // 1000000

dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (ano % 400 == 0) or (ano%4 == 0 and ano%100 != 0):
	dias[1] = 29

if ano < 1:
	print(dia, 'de', mes, 'de', ano, 'nao eh uma data valida')
elif mes < 1 or mes > 12:
	print(dia, 'de', mes, 'de', ano, 'nao eh uma data valida')
elif dia < 1 or dia > dias[mes - 1]:
	print(dia, 'de', mes, 'de', ano, 'nao eh uma data valida')
elif ano == 1582 and mes == 10 and (dia >= 5 and dia <=14):
	print(dia, 'de', mes, 'de', ano, 'nao eh uma data valida')
else:
	print(dia, 'de', mes, 'de', ano, 'eh uma data valida')