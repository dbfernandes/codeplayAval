
c1 = float(input())
c2 = float(input())
c3 = float(input())
c4 = float(input())
c5 = float(input())
c6 = float(input())

p1 = c1/c2
p2 = c3/c4
p3 = c5/c6

s1 = abs(p1 - p2)
s2 = abs(p1 - p3)
s3 = abs(p2 - p3)

if(s1 < s2 and s1 < s3):
	print('1 e 2')
elif(s2 < s1 and s2 < s3):
	print('1 e 3')
else:
	print('2 e 3')