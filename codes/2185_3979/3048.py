from numpy import *
n = int(input("Digite um numero: "))
num = str(n).zfill(5)
u = num[-1]
d = num[-2]
c = num[-3]
m = num[-4]
dm = num[-5]
unid = array(["zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove"])
dez = array(["dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove"])
dezn = array(["dez","vinte","trinta","quarenta","cinquenta","sessenta","setenta","oitenta","noventa"])
cent = array(["cem","duzentos","trezentos","quatrocentos","quinhentos","seiscentos","setecentos","oitocentos","novecentos"])
if(n == 10000):
	ext = "dez mil"
else:
	if(int(d) == 0):
		dez_ext = ""
		un_ext = unid[int(u)]
	elif(int(d) == 1) and (int(u) > - 1) and (int(u) < 10):
		dez_ext = dez[int(u)]
		un_ext = ""
	else:
		dez_ext = dezn[int(d) - 1] + " " + "e" + " "
		un_ext = unid[int(u)]
	if(int(c) == 0):
		cent_ext = ""
	elif(int(c) == 1):
		cent_ext = "cento" + " " + "e" + " "
	else:
		cent_ext = cent[int(c) - 1] + " " + "e" + " "
	if(int(m) == 0):
		m_ext = ""
	elif(int(m) == 1):
		m_ext = "mil e" + " "
	else:
		m_ext = unid[int(m)] + " "  + "mil e" + " "

	ext = m_ext + cent_ext + dez_ext + un_ext
print(ext)