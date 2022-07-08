a=input("String:")
b=len(a)
c=""
for i in range(b):
	if((a[i]!="a")and(a[i]!="A")):
		c=c+a[i]
print(c)