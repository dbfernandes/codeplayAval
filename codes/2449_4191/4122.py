a=float(input("Variavel a"))
b=float(input("Variavel b"))
c=float(input("Variavel c"))
d=float(input("Variavel d"))
e=float(input("Variavel e"))
f=float(input("Variavel d"))
if((a*e)-(b*d)==0):
	print('Nao tem solucao')
else:
	x=((c*e)-(b*f))/((a*e)-(b*d))
	y=((a*f)-(c*d))/((a*e)-(b*d))
	print(x)
	print(y)