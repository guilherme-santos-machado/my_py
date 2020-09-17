import pandas as pd 

df = pd.read_csv('./teste.csv', low_memory=False, header = 1)

df.to_csv('teste2.csv')