from numpy import*
from numpy.linalg import*
m = array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])
n = array([50,-120,350,870])
n = n.T
res = solve(m,n)

print(res)