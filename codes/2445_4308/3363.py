escala = input("(C)Celsius ou (F)Fahrenheit: ")
temp = float(input("temperatura: "))

if (escala == "F"):
	conv = (5/9) * (temp - 32)
if (escala == "C"):
	conv = (9*temp + 160) / 5
	
print(round(conv, 2))