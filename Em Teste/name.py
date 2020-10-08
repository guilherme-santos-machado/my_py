import pandas as pd
import numpy as np
import os
import shutil

source = './'
files = os.listdir(source)
for file in files:
    extensao = file.split('.')[1]
    nameFile = file.split('.')[0]
    print(nameFile)
