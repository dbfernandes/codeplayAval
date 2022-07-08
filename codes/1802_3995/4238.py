import math
var=int(input("vida:"))
D1=int(input("d1:"))
D2=int(input("d2:"))
dano=(5*D1)**0.5 + math.pi**(D2/3)
x=var-int(dano)
print(x)