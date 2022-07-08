temp = float(input("1.Digite o valor da temperatura do ar em graus Celsius(C): "))
vent = float(input("2.Digite o valor da velocidade do vento em km/h: "))

if (temp > -50) and (temp < 10): 
	if (vent > 4.8):
		sigma = 13.12 + 0.6215*temp - (11.37*vent**0.16) + (0.3965*temp*vent**0.16)
		print(round(sigma, 4))
	else:
		print("Velocidade invalida")
else:
	print("Temperatura invalida")
	if (vent <= 4.8):	
		print("Velocidade invalida")