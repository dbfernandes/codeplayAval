from math import *

olho1 = float(input())
nariz1 = float(input())
olho2 = float(input())
nariz2 = float(input())
olho3 = float(input())
nariz3 = float(input())

razao1 = olho1/nariz1
razao2 = olho2/nariz2
razao3 = olho3/nariz3

if abs(razao1 - razao2) < abs(razao1 - razao3):
	if abs(razao1 - razao2) < abs(razao2 - razao3):
		print("1 e 2")
	else:
		print("2 e 3")
else:
	if abs(razao1 - razao3) < abs(razao2 - razao3):
		print('1 e 3')
	else:
		print('2 e 3')