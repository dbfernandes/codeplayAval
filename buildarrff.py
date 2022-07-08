import os
from datetime import datetime, time, timedelta

arff_path = "./plagio.arff"
rotulos_csv = "./rotulos.csv"
rotulos_path = "./dataset/"
dataset_path = "./2019-1/"
submissoes_csv = "./submissao.csv"
codes_path = "./codes/"
ano = "2019"

attributes = """@relation Plagio
@attribute 'logins' numeric
@attribute 'log_size' numeric
@attribute 'input' numeric
@attribute 'backspace' numeric
@attribute 'test' numeric
@attribute 'error_test' numeric
@attribute 'submition' numeric
@attribute 'error_submition' numeric
@attribute 'navegation' numeric
@attribute 'exercise_time' numeric
@attribute '%_paste' numeric
@attribute '%_alunos_acertaram' numeric
@attribute '%_atividades_corretas' numeric
@attribute 'procrastinacao' numeric
@attribute 'media_avaliacoes' numeric
@attribute 'diff_avaliacoes_listas' numeric
@attribute 'plagio' {'sim', 'nao'}
@data
"""

arff_file = open(arff_path, 'w')
arff_file.writelines(attributes)

rotulos_file = open(rotulos_csv, 'r')
rotulos = rotulos_file.readlines()

start_trabalhos = {}
end_trabalhos = {}
type_trabalhos = {}

for rotulo in rotulos:
    
    exercicio = rotulo.strip().split(",")[0].split("_")[0]
    aluno_original = rotulo.strip().split(",")[0].split("_")[1]
    rotulo = rotulo.strip().split(",")[1]    
    total_trabalhos_turma = 0
    total_exercicios_turma = 0
    alunos = {}

    for subdir, dirs, files in os.walk(rotulos_path):

        for filename in files:

            if subdir.endswith(f"{exercicio}_{aluno_original}") and filename.endswith(".py"):

                alunos[filename.replace(".py","")] = 0

    for aluno in alunos:

        submissoes_file = open(submissoes_csv, 'r')
        submissoes_data = submissoes_file.readlines()

        for submissao in submissoes_data:
            
            submissao_array = submissao.split(",")
            if (exercicio == submissao_array[0] and aluno == submissao_array[1]):
                alunos[aluno] = submissao_array[3].strip()
    

    print(alunos)
    alunos_array = []
    for key, value in alunos.items():
        alunos_array.append(key)

    data_submissao_aluno0 = datetime.strptime(alunos[alunos_array[0]], '%Y-%m-%d %H:%M:%S')
    data_submissao_aluno1 = datetime.strptime(alunos[alunos_array[1]], '%Y-%m-%d %H:%M:%S')    
    
    if (data_submissao_aluno0 > data_submissao_aluno1):
        aluno = alunos_array[0]
    else:
        aluno = alunos_array[1]

    print(exercicio, aluno, rotulo)

    # Pegando o id da turma
    for subdir, dirs, files in os.walk(dataset_path):

        for filename in files:

            if subdir.endswith(f"users/{aluno}"):

                subdir_data = subdir.split("/")
                turma = subdir_data[2]
                break

    # Pegando a data de inicio dos trabalhos da turma
    for subdir, dirs, files in os.walk(dataset_path):

        for filename in files:

            if subdir.endswith(f"{turma}/assessments"):

                total_trabalhos_turma = total_trabalhos_turma + 1
                assessment_file = open(subdir + "/" + filename, 'r')
                assessment_data = assessment_file.readlines()
                trabalho = filename.replace(".data","")

                for data in assessment_data:

                    if "---- exercise " in data:
                        total_exercicios_turma = total_exercicios_turma + 1

                    if "---- type: " in data:
                        type = data.replace("---- type: ", "")
                        type = type.strip()
                        type_trabalhos[int(trabalho)] = type

                    if "---- start: " in data:
                        start = data.replace("---- start: ", "")
                        start = start.strip()
                        start_trabalhos[int(trabalho)] = datetime.strptime(start, '%Y-%m-%d %H:%M')

                    if "---- end: " in data:
                        end = data.replace("---- end: ", "")
                        end = end.strip()
                        end_trabalhos[int(trabalho)] = datetime.strptime(end, '%Y-%m-%d %H:%M')                        

    for subdir, dirs, files in os.walk(dataset_path):

        for filename in files:                

            if subdir.endswith(f"{turma}/users/{aluno}") and filename.endswith("logins.log"):

                logins_file = open(subdir + "/" + filename, 'r')
                logins_data = logins_file.readlines()
                qtd_logins = 0

                ##### quantidade de logins #####      

                for logins in logins_data:
                    if (logins.startswith(ano) and "login" in logins):
                        qtd_logins = qtd_logins + 1

                arff_file.write(str(qtd_logins) + ",")    

            if subdir.endswith(f"{turma}/users/{aluno}/codemirror") and filename.endswith(f"{exercicio}.log"):

                codemirror_file = open(subdir + "/" + filename, 'r')
                codemirror_data = codemirror_file.readlines()

                ##### tamanho dos logs #####   

                log_size = len(codemirror_data)
                arff_file.write(str(log_size) + ",")

                ##### número de inputs #####   

                token = "+input"
                contador = 0
                for log in codemirror_data:
                    if token in log:
                        contador = contador + 1
                arff_file.write(str(contador) + ",")


                ##### número de deletes e backspaces #####   

                token1 = "+delete"
                token2 = "Backspace"
                contador = 0
                for log in codemirror_data:
                    if (token1 in log) or (token2 in log):
                        contador = contador + 1
                arff_file.write(str(contador) + ",")

                ##### quantidade de testes #####   

                token = "#saida_testar#"
                contador = 0
                for log in codemirror_data:
                    if token in log:
                        contador = contador + 1                       
                arff_file.write(str(contador) + ",")                

                ##### quantidade de erros nos testes #####   

                token = "Error:"
                contador = 0
                for log in codemirror_data:
                    if token in log:
                        contador = contador + 1                       
                arff_file.write(str(contador) + ",")                

                ##### quantidade de submissoes #####   

                token = "#submit#"
                contador = 0
                for log in codemirror_data:
                    if token in log:
                        contador = contador + 1                       
                arff_file.write(str(contador) + ",")   

                ##### quantidade de erros nas submissoes #####   

                token = "#submit#Your code did not produce"
                contador = 0
                for log in codemirror_data:
                    if token in log:
                        contador = contador + 1                       
                arff_file.write(str(contador) + ",")      

                ##### navegacao no código #####   

                token1 = '#"Up"'
                token2 = '#"Right"'
                token3 = '#"Down"'                
                token4 = '#"Left"'

                contador = 0
                for log in codemirror_data:
                    if (token1 in log) or (token2 in log) or (token3 in log) or (token4 in log):
                        contador = contador + 1
                arff_file.write(str(contador) + ",")

                ##### tempo de resolução do exercicio ##### 

                primeiraInteracao = 1
                segundosValidos = timedelta(hours=0,minutes=0,seconds=0)
                segundosInvalidos = timedelta(hours=0,minutes=0,seconds=0)

                for log in codemirror_data:

                    if primeiraInteracao == 1:
                        dataHorarioAtual = log[0:17]
                        dataHorario = datetime.strptime(dataHorarioAtual, '%Y-%m-%d %H:%M:%S')
                        dataHorarioAnterior = dataHorario
                        primeiraInteracao = 0
                    else:
                        dataHorarioAtual = log[0:17]
                        try:
                            dataHorario = datetime.strptime(dataHorarioAtual, '%Y-%m-%d %H:%M:%S')
                            diferencaHorario = dataHorario - dataHorarioAnterior
                            dataHorarioAnterior = dataHorario
                            if diferencaHorario > timedelta(seconds=60) or diferencaHorario == timedelta(hours=0,minutes=0,seconds=0):
                                #print(diferencaHorario)
                                segundosInvalidos = segundosInvalidos + diferencaHorario
                            else:
                                #print("Valido: ", linha)
                                #print("Diferenca: ", diferencaHorario)

                                segundosValidos = segundosValidos + diferencaHorario
                                #print("Segundos Validos: ", segundosValidos)
                        except:
                            pass                

                arff_file.write(str(segundosValidos.total_seconds()) + ",")

                ##### proporçao paste/size(code) ##### 

                token = '"origin":"paste"'
                array_pastes = []
                for log in codemirror_data:
                    if token in log:
                        array_pastes.append(len(log)-154) # 154 é o tamanho tipico do texto desse registro, qdo se tira o conteudo copiado

                if array_pastes:
                    code_file = open(rotulos_path + exercicio +"_"+ aluno_original + "/" + aluno + ".py", 'r')
                    code_code = code_file.read()                    
                    arff_file.write(str(round(max(array_pastes)/len(code_code),2)) + ",")
                else:
                    arff_file.write(str(0) + ",")

    ##### proporcao de alunos que acertaram o exercicio ##### 

    total_tentativas = 0
    total_acertos = 0

    for subdir, dirs, files in os.walk(dataset_path):

        for filename in files:

            if subdir.endswith(f"codemirror") and filename.endswith(f"{exercicio}.log"):

                total_tentativas = total_tentativas + 1
                
                codemirror_file = open(subdir + "/" + filename, 'r')  
                codemirror_data = codemirror_file.read()
                if "Congratulations" in codemirror_data:
                    total_acertos = total_acertos + 1

    if total_acertos > 0:
        arff_file.write(str(round(total_acertos/total_tentativas,2)) + ",")
    else:
        arff_file.write("0,")

    ##### proporcao de atividades corretas #####

    total_exercicios = 0
    total_acertos = 0

    total_tentativas = 0
    total_acertos = 0

    print(total_trabalhos_turma)
    print(total_exercicios_turma)

    for subdir, dirs, files in os.walk(dataset_path):

        for filename in files:

            if subdir.endswith(f"{turma}/users/{aluno}/codemirror") and filename.endswith(".log"):

                total_tentativas = total_tentativas + 1

    submissoes_file = open(submissoes_csv, 'r')
    submissoes_data = submissoes_file.readlines()

    for submissao in submissoes_data:
        
        submissao_array = submissao.split(",")
        if (aluno == submissao_array[1]):
            total_acertos = total_acertos + 1


    if total_acertos > 0:
        arff_file.write(str(round(total_acertos/total_exercicios_turma,2)) + ",")
    else:
        arff_file.write("0,")

    ##### indice de procrastinacao ##### 

    tempo_total = 0

    submissoes_file = open(submissoes_csv, 'r')
    submissoes_data = submissoes_file.readlines()

    for submissao in submissoes_data:
        
        submissao_array = submissao.split(",")

        if (aluno == submissao_array[1]):
            trabalho = submissao_array[2] 
            hora = submissao_array[3].strip()
            hora = datetime.strptime(hora, '%Y-%m-%d %H:%M:%S')

            if int(trabalho) in end_trabalhos:
                timediff = end_trabalhos[int(trabalho)] - hora
                if timediff:
                    tempo_total = tempo_total + (timediff.days * 24 * 3600 + timediff.seconds)/3660

    if tempo_total > 0:
        arff_file.write(str(round(tempo_total,2)) + ",")
    else:
        arff_file.write("0,")                        


    ##### notas avaliações ##### 

    soma_notas_exames = 0
    qtd_exames = 0
    soma_notas_listas = 0
    qtd_listas = 0

    for subdir, dirs, files in os.walk(dataset_path):

        for filename in files:

            if subdir.endswith(f"{turma}/users/{aluno}/grades") and filename.endswith("final_grade.data"):

                assessment_file = open(subdir + "/" + filename, 'r')
                final_grade = assessment_file.read().strip()

    arff_file.write(final_grade + ",")

    ##### nota listas - avaliações ##### 

    soma_notas_exames = 0
    qtd_exames = 0
    soma_notas_listas = 0
    qtd_listas = 0

    for subdir, dirs, files in os.walk(dataset_path):

        for filename in files:

            if subdir.endswith(f"{turma}/users/{aluno}/grades") and filename.endswith(".log"):

                assessment_file = open(subdir + "/" + filename, 'r')
                assessment_data = assessment_file.readlines()
                trabalho = filename.replace(".log","")

                total_trabalhos_turma = total_trabalhos_turma + 1

                for data in assessment_data:

                    if "---- grade (0-10): " in data:
                        final_score = data.replace("---- grade (0-10): ","")
                        final_score = final_score.strip()

                if "exam" in type_trabalhos[int(trabalho)]:
                    soma_notas_exames = soma_notas_exames + float(final_score)
                    qtd_exames = qtd_exames + 1
                else:
                    soma_notas_listas = soma_notas_listas + float(final_score)
                    qtd_listas = qtd_listas + 1                    

    if qtd_exames>0 and qtd_listas>0:
        media_exames = soma_notas_exames/qtd_exames      
        media_listas = soma_notas_listas/qtd_listas 
        arff_file.write(str(round(media_listas - media_exames,2)) + ",")
    else:
        arff_file.write("0,") 

    arff_file.write(rotulo + " % " + exercicio + "_" + aluno_original + "/" + aluno + " tur:" + turma + " trab:" + trabalho + "\n")


arff_file.close()
rotulos_file.close()

