from numpy import *
from numpy.linalg import *

matriz = array(eval(input(":")))



for i in range(shape(matriz)[0]):
		print(max(matriz[i,:]))
