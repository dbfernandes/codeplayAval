from math import *
x = int(input())
i = 4
while(i <= x):
	if(i % 2 != 0):
		perimetro = sin(pi/i)/sin((3*pi)/(2*i))
	else:
		perimetro = sin(pi/i)/sin(2*pi/i)
	print('{} {}'.format(i,round(perimetro,4)))
	i = i + 1