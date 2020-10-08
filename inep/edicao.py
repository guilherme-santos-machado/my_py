import xlrd
import pandas as pd
import numpy as np

#Projeto Pandas
df = pd.read_excel('./ATU_ESCOLAS_2018.xlsx')

#Limpar cabeçalho e base
df.drop(df.head(7).index,inplace=True)    
df.drop(df.tail(3).index,inplace=True)
df.to_csv('teste.csv')


df = pd.read_csv('./teste.csv', low_memory=False, header=1, index_col=1)
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.drop(columns=['7'])


df.replace({'--': np.nan}, inplace=True)

print(df)

df.to_csv('teste.csv')


    


