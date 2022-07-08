# Universidade Federal do Amazonas
# Ysraele Duany Barreto Feitosa
# Data: 26/03/2019
# -----------------------------
from math import *
# latitude no ponto 1
t1 = radians(float(input("Latitude de P1: ")))
# longitude no ponto 1
g1 =  radians(float(input("Longitude de P1: ")))
# latidtude no ponto 2
t2 = radians(float(input("Latitude de P2: ")))
# longitude no ponto 2
g2 = radians(float(input("Longitude de P2: ")))
# raio médio da terra em km
r = 6371.01
# distância entre os dois pontos
d = r*acos((sin(t1)*sin(t2)) + (cos(t1)*cos(t2)*cos(g1-g2)))

print(round(d, 2))



