# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
valor=int(input("Cedula de:"))
print("Entrada:", valor)
if(valor==2):
	print("Animal: Tartaruga")
else:
	if(valor==5):
		print("Animal: Garca")
	else:
		if(valor==10):
			print("Animal: Arara")
		else:
			if(valor==20):
				print("Animal: Mico-leao-dourado")
			else:
				if(valor==50):
					print("Animal: Onca-pintada")
				else:
					if(valor==100):
						print("Animal: Garoupa")
					else:
						print("Animal: Invalido")