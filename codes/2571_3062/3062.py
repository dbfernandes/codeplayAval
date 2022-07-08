x = input("String: ")
v = ""
a=0
i=0
while(i < len(x)):
	if(x[i].upper() != 'A'):
		v = v + x[i] 
	i=i+1
print(v)