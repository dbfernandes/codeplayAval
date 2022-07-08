import time

arff = "./dataset.arff"
arff_new = "./dataset_new.arff"
arff_index = 0
arff_size = 2

def timeCongratulation(file):

    with open(file) as f:

        contents = f.readlines()

        for line in contents:

            if "Congratulations" in line: 

                return line.split(".")[0]

fnew = open(arff_new, "w")  

with open(arff) as f:

    arff_data = f.readlines()

    for arff_index in range(0, arff_size, 2):

        time_cong_1 = timeCongratulation(arff_data[arff_index].strip())
        time_cong_2 = timeCongratulation(arff_data[arff_index+1].strip())

        print(time_cong_1)
        print(time_cong_2)

        if (time_cong_1 > time_cong_2):
            fnew.write(arff_data[arff_index].strip())
        else:
            fnew.write(arff_data[arff_index+1].strip())

fnew.close()



