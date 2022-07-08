import os
import os.path
import subprocess
import time
import urllib.request
from bs4 import BeautifulSoup
import re

dataset_path = "/home/david/dev/moss/dataset/"
moss_command = ["/home/david/dev/moss/moss.pl","-l","python"]

for currentpath, folders, files in os.walk(dataset_path):

    if currentpath == dataset_path:
        continue

    if not os.path.exists(currentpath + '/moss.html'):  

        time.sleep(10) # Sleep for 10 seconds    

        command = moss_command.copy()

        for file in files:
            if file.endswith('.py'):
                command.append(os.path.join(currentpath, file))

        result = subprocess.run(command, stdout=subprocess.PIPE)
        result = result.stdout.decode("utf-8")
        result_url = result.split()[-1]
        result_url_contents = urllib.request.urlopen(result_url).read()
        result_url_contents = result_url_contents.decode("utf-8")

        with open(currentpath + '/moss.html', 'w') as f:
            f.write(result_url_contents)
    
    else:
        
        with open(currentpath + '/moss.html', 'r') as f:
            result_url_contents = f.read()
    
    soup = BeautifulSoup(result_url_contents, 'html.parser')
    percentage = soup.find_all('a')[-1]
    percentage = re.sub('<[^<]+?>', '', str(percentage))
    percentage = re.sub('[^0-9]','', percentage.split()[-1])
    
    if not percentage:
        percentage = "0"

    print(percentage)

    with open(currentpath + '/moss_percentage.txt', 'w') as f:
        f.write(percentage)    
 

