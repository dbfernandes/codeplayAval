import os
import os.path

dataset = "/home/david/dev/moss/dataset/"
rotulos = "/home/david/dev/moss/rotulos.csv"
threshold = 90
tn = 0
tp = 0
fn = 0
fp = 0

total_plagio = 32
total_nao_plagio = 68

for threshold in range(50, 100, 10):

    print("Threshold: ", threshold)

    for currentpath, folders, files in os.walk(dataset):

        for file in files:

            if file.endswith('percentage.txt'):

                with open(currentpath + '/' + file, 'r') as f:
                    percentage = f.read().strip()
                    percentage = int(percentage)

                id = currentpath.split('/')[-1]
                
                with open(rotulos, 'r') as f:

                    for rotulo in f.readlines():

                        rotulo_id = rotulo.split(',')[0].strip()
                        rotulo_value = rotulo.split(',')[1].strip()

                        if (rotulo_id == id):
        
                            if (percentage < threshold): # classificacao = nao

                                if (rotulo_value == "nao"):
                                    tn = tn + 1
                                elif (rotulo_value == "sim"):
                                    fn = fn + 1     

                            else:                       # classificacao = sim

                                if (rotulo_value == "nao"):
                                    fp = fp + 1
                                elif (rotulo_value == "sim"):
                                    tp = fp + 1   
    
    print("Verdadeiro positivo: ", tp)
    print("Falso positivo: ", fp)
    print("Verdadeiro negativo: ", tn)
    print("Falso negativo: ", fn)

    precisao_plagio = tp/(tp+fp)
    precisao_nao_plagio = tn/(tn+fn)

    revocacao_plagio = tp/(tp+fn)
    revocacao_nao_plagio = tn/(tn+fp)

    f1_plagio = 2*precisao_plagio*revocacao_plagio/(precisao_plagio+revocacao_plagio)
    f1_nao_plagio = 2*precisao_nao_plagio*revocacao_nao_plagio/(precisao_nao_plagio+revocacao_nao_plagio)

    precisao_media = (precisao_plagio*total_plagio + precisao_nao_plagio*total_nao_plagio)/(total_plagio+total_nao_plagio)
    revocacao_media = (revocacao_plagio*total_plagio + revocacao_nao_plagio*total_nao_plagio)/(total_plagio+total_nao_plagio)
    f1_medio = (f1_plagio*total_plagio + f1_nao_plagio*total_nao_plagio)/(total_plagio+total_nao_plagio)


    print("Precisao Plagio:", precisao_plagio)
    print("Revocacao Plagio:", revocacao_plagio)
    print("F1 Plagio:", f1_plagio)
    print()
    print("Precisao nao Plagio:", precisao_nao_plagio)
    print("Revocacao nao Plagio:", revocacao_nao_plagio)
    print("F1 nao Plagio:", f1_nao_plagio)  
    print()
    print("Precisao media:", precisao_media)
    print("Revocacao media:", revocacao_media)
    print("F1 medio:", f1_medio)        

    print()
    print()

