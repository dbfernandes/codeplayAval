temp = float(input("temperatura do ar: "))
vento = float(input("velocidade do vento: "))
if (temp > -50) and (temp < 10):
	if (vento > 4.8):
		sigma = 13.12 + 0.6215 * temp - (11.37 * vento**0.16) + (0.3965 * temp * vento**0.16)
		print(round(sigma, 4))
	else:
		print("Velocidade invalida")
else:
	print("Temperatura invalida")
	if (vento <= 4.8):
		print("Velocidade invalida")