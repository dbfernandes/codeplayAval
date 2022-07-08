from numpy import *
a = array(eval(input()))
b = array(eval(input()))
c = array(zeros(size(a),dtype = float))
for i in range(0,size(a)):
	c[i]= round((a[i]/(b[i])**2),2)
	
print(c)
print("O MAIOR IMC DA TURMA EH: ",round(max(c),2))
d = round(max(c),2)
if(d<17):
	print("MUITO ABAIXO DO PESO")
elif(d>=17 and d<18.49):
	print("ABAIXO DO PESO")
elif(d>=18.5 and d<24.99):
	print("PESO NORMAL")
elif(d>=25 and d<29.99):
	print("ACIMA DO PESO")
elif(d>=30 and d<34.99):
	print("OBESIDADE")
elif(d>=35 and d<39.99):
	print("OBESIDADE SEVERA")
elif(d>40):
	print("OBESIDADE MORBIDA")