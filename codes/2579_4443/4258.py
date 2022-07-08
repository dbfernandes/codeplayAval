from numpy import *
s = input("String: ")

n = 50
h = 0
if(s == "Calcule"):
	for i in range(0, n):
		h = h + ((2*i + 1)/(i + 1))
print(round(h,2))