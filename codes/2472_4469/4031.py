q1 = input("resposta do aluno para a questao 1: ")
q2 = input("resposta do aluno para a questao 2: ")
q3 = input("resposta do aluno para a questao 3: ")
r1 = input("gabarito da questao 1: ")
r2 = input("gabarito da questao 2: ")
r3 = input("gabariot da questao 3: ")
acertos = 0
if (q1 == r1):
	acertos = acertos + 1
if (q2 == r2):
	acertos = acertos + 1
if (q3 == r3):
	acertos = acertos + 1
print(acertos)