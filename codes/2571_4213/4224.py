
p=input(".")
c=len(p)
u=" "
for i in range(c):
	if((p[i]!='a')and (p[i]!='A')):
		u=u+p[i]
print(u)	