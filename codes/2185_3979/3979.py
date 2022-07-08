num = int(input())

dign = ['um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']
dezn = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
centn = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

out = ''

if num == 10000:
	out += 'dez mil'
else:
	mil = num // 1000
	cent = (num % 1000) // 100
	dez = (num % 100) // 10
	un = num % 10
		
	if num == 1000:
		out += 'mil'
	else:
		if mil == 1:
			out += 'mil e '
		elif mil > 1:
			out += dign[mil - 1] + ' mil'
			if (cent != 0 or dez != 0 or un !=0):
				out += ' e '
			
		if num % 1000 == 100:
			out += 'cem'
		elif cent > 0:
			out += centn[cent - 1]
			if (dez != 0 or un != 0):
				out += ' e '
		
		if dez > 1:
			out += dezn[dez - 1]
			if (un != 0):
				out += ' e '
				out += dign[un - 1]
		elif dez > 0 or un > 0:
			out += dign[dez*10+un - 1]

print(out)