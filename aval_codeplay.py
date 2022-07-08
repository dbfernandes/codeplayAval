import os
from datetime import datetime
import csv
import sys

if len(sys.argv) != 3:
    print("pyton3 aval_codeplay.py <ano> <semestre>")
    quit()

ano = sys.argv[1]
semestre = sys.argv[2]

dataset_path = f"./{ano}-{semestre}"
csv_folder = f"./csv-{ano}-{semestre}"

monitores_e_professores = [1071,6091,1083,6527,2083,6280,3009,6370,3853,6283,105,1997,6276,6296,5994,3500,7096,2087,7078,5724,670,7095,2805,7079,14,6985,6961,7077,13,7081]  

if not os.path.exists(csv_folder):
  os.mkdir(csv_folder)

trabalhos = {}

fieldnames = ['id_aluno', 'logins', 'tamanho_logs_listas', 'tamanho_logs_avaliacoes', 'total_testes_listas', 'total_testes_avaliacoes', 'total_erros_sintaticos_testes_listas', 'total_erros_sintaticos_testes_avaliacoes', 'total_submissoes_listas', 'total_submissoes_avaliacoes', 'total_submissoes_incorretas_listas', 'total_submissoes_incorretas_avaliacoes', 'indice_procrastinacao_listas']

for turma in os.listdir(dataset_path):
  print(turma)
  total_trabalhos_turma = 0
  total_exercicios_turma = 0

  # Pegando a data de inicio dos trabalhos da turma
  for subdir, dirs, files in os.walk(f"{dataset_path}/{turma}"):

    for filename in files:

      if subdir.endswith("assessments"):

        total_trabalhos_turma = total_trabalhos_turma + 1
        assessment_file = open(subdir + "/" + filename, 'r')
        assessment_data = assessment_file.readlines()
        trabalho = filename.replace(".data","")
        trabalhos[trabalho] = {
          'type': '',
          'start': '',
          'end': '',
          'lab0': False
        }

        for data in assessment_data:

          if "assessment title: Lab 0 " in data:
            trabalhos[trabalho]['lab0'] = True         

          if "---- exercise " in data:
            total_exercicios_turma = total_exercicios_turma + 1

          if "---- type: " in data:
            type = data.replace("---- type: ", "")
            type = type.strip()
            trabalhos[trabalho]['type'] = type

          if "---- start: " in data:
            start = data.replace("---- start: ", "")
            start = start.strip()
            trabalhos[trabalho]['start'] = datetime.strptime(start, '%Y-%m-%d %H:%M')

          if "---- end: " in data:
            end = data.replace("---- end: ", "")
            end = end.strip()
            trabalhos[trabalho]['end'] = datetime.strptime(end, '%Y-%m-%d %H:%M')                                       

  with open(f"{csv_folder}/{turma}.csv", 'w') as csv_turma:

    csv_turma_writer = csv.DictWriter(csv_turma, fieldnames=fieldnames)
    csv_turma_writer.writeheader()

    # ID do aluno
    for aluno in os.listdir(f"{dataset_path}/{turma}/users"):

      if aluno in monitores_e_professores:
        continue

      minutos_entre_submissao_e_fim_do_trabalho = 0
      quantidade_total_exercicios = 0

      aluno_data = {
        'id_aluno': aluno,
        'logins': 0,
        'tamanho_logs_listas': 0,
        'tamanho_logs_avaliacoes': 0,
        'total_testes_listas': 0,
        'total_testes_avaliacoes': 0,        
        'total_erros_sintaticos_testes_listas': 0,
        'total_erros_sintaticos_testes_avaliacoes': 0,        
        'total_submissoes_listas': 0,
        'total_submissoes_avaliacoes': 0,        
        'total_submissoes_incorretas_listas': 0,
        'total_submissoes_incorretas_avaliacoes': 0,   
        'indice_procrastinacao_listas': 0
      }      

      # quantidade de logins
      for subdir, dirs, files in os.walk(f"{dataset_path}/{turma}/users/{aluno}"):

        for filename in files:                

          ##### ARQUIVO: arquivo de logins/logouts #####
          if subdir.endswith(f"{turma}/users/{aluno}") and filename.endswith("logins.log"):

            logins_file = open(subdir + "/" + filename, 'r')
            logins_data = logins_file.readlines()  

            ##### DATA: quantidade de logins #####   
            for logins in logins_data:
              if (logins.startswith(ano) and "login" in logins):
                aluno_data['logins'] = aluno_data['logins'] + 1


          ##### ARQUIVO: logs do codemirror #####
          if subdir.endswith(f"{turma}/users/{aluno}/codemirror"):

            quantidade_total_exercicios = quantidade_total_exercicios + 1

            codemirror_file = open(subdir + "/" + filename, 'r')
            codemirror_data = codemirror_file.readlines()
            id_trabalho = filename.split(".")[0].split("_")[0]
            # print(filename, id_trabalho, aluno)

            # Ignorando os Labs 0 (de ambientação)
            if (trabalhos[id_trabalho]['lab0'] == True):
              continue

            ##### DATA: tamanho dos logs #####   
            log_size = len(codemirror_data)
            if (trabalhos[id_trabalho]['type'] == 'homework'):
              aluno_data['tamanho_logs_listas'] = aluno_data['tamanho_logs_listas'] + log_size       
            else:
              aluno_data['tamanho_logs_avaliacoes'] = aluno_data['tamanho_logs_avaliacoes'] + log_size

            for log in codemirror_data:
              
              ##### DATA: quantidade de testes #####   
              token_total_testes_listas = "#saida_testar#"
              if token_total_testes_listas in log:
                if (trabalhos[id_trabalho]['type'] == 'homework'):
                  aluno_data['total_testes_listas'] = aluno_data['total_testes_listas'] + 1                       
                else:
                  aluno_data['total_testes_avaliacoes'] = aluno_data['total_testes_avaliacoes'] + 1                       

              ##### DATA: quantidade de erros sintaticos nos testes #####   
              token_total_erros_sintaticos_testes_listas = "Error:"
              if token_total_erros_sintaticos_testes_listas in log:
                if (trabalhos[id_trabalho]['type'] == 'homework'):
                  aluno_data['total_erros_sintaticos_testes_listas'] = aluno_data['total_erros_sintaticos_testes_listas'] + 1  
                else:
                  aluno_data['total_erros_sintaticos_testes_avaliacoes'] = aluno_data['total_erros_sintaticos_testes_avaliacoes'] + 1  

              ##### DATA: quantidade de submissoes #####   
              token_total_submissoes_listas = "#submit#"
              if token_total_submissoes_listas in log:
                if (trabalhos[id_trabalho]['type'] == 'homework'):
                  aluno_data['total_submissoes_listas'] = aluno_data['total_submissoes_listas'] + 1
                  hora_submissao = log.split(".")[0]
                  hora_submissao = datetime.strptime(hora_submissao, "%Y-%m-%d %H:%M:%S")
                  minutos_entre_submissao_e_fim_do_trabalho = minutos_entre_submissao_e_fim_do_trabalho + (trabalhos[id_trabalho]['end'] - hora_submissao).total_seconds()/60                  
                else:
                  aluno_data['total_submissoes_avaliacoes'] = aluno_data['total_submissoes_avaliacoes'] + 1

              ##### DATA: quantidade de submissoes incorretas #####   
              token_total_submissoes_incorretas_listas = "#submit#Your code did not produce"
              if token_total_submissoes_incorretas_listas in log:
                if (trabalhos[id_trabalho]['type'] == 'homework'):
                  aluno_data['total_submissoes_incorretas_listas'] = aluno_data['total_submissoes_incorretas_listas'] + 1  
                else:
                  aluno_data['total_submissoes_incorretas_avaliacoes'] = aluno_data['total_submissoes_incorretas_avaliacoes'] + 1          

      aluno_data['indice_procrastinacao_listas'] = round(minutos_entre_submissao_e_fim_do_trabalho / aluno_data['total_submissoes_listas'], 2) if aluno_data['total_submissoes_listas'] > 0 else 0
      if (aluno_data['indice_procrastinacao_listas'] > 20000):
        print(aluno_data['indice_procrastinacao_listas'])

      csv_turma_writer.writerow(aluno_data)

