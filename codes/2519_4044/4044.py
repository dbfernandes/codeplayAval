alt_total = int(input("Altura total da Torre presente na Lua(metros): "))
v_acima = int(input("Quantidade de metros/minuto que Equecrates sobe ate a Torre: "))
v_abaixo = int(input("Quantidade de metros/minuto que Antistines ocasiona a descida: "))

tempo = 0
dist = 0

while (dist < alt_total):
	tempo += 1
	dist += v_acima	
	
	if (dist) < (alt_total):
		dist -= v_abaixo			
		
print("%d" %tempo)
