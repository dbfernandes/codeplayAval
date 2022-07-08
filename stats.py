import os
import os.path
import subprocess
import time
import urllib.request
from bs4 import BeautifulSoup
import re

dataset_path = "/home/david/dev/moss/dataset/"
lines = 0

for currentpath, folders, files in os.walk(dataset_path):

    if currentpath == dataset_path:
        continue

    for file in files:

        if file.endswith('.py'):

            with open(os.path.join(currentpath, file), 'r') as f:

                for sourcecode in f.readlines():        

                    lines = lines+1

print("Numero de linhas: ", lines/200)
