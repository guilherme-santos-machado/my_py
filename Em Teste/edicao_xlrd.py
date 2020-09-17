import xlrd
import pandas as pd

#Projeto Pandas
df = pd.read_excel('./ATU_ESCOLAS_2018.xlsx')

#Limpar cabeçalho e base
df.drop(df.head(7).index,inplace=True)    
df.drop(df.tail(2).index,inplace=True)
df.to_csv('teste.csv')


df = pd.read_csv('./teste.csv', low_memory=False, header = 1)

print(df)
df.to_csv('teste2.csv')


    


