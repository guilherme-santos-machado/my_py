#Importação de bibliotecas
import xlrd
import pandas as pd
import numpy as np

#Projeto Pandas
#Pega o arquivo e importa para o Pandas
df = pd.read_excel('./ATU_ESCOLAS_2018.xlsx')

#Limpar cabeçalho e base
df.drop(df.head(7).index,inplace=True)    
df.drop(df.tail(3).index,inplace=True)
#Salva o arquivo em formato CSV
df.to_csv('teste.csv')

#Faz a leitura do arquivo csv e aponta o head e index
df = pd.read_csv('./teste.csv', low_memory=False, header=1, index_col=1)
#Apaga qualquer coluna sem nome
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
#Faz o drop da coluna com o nome "7"
df = df.drop(columns=['7'])

#Faz a substituição do "--" e mantem o campo como "null"
df.replace({'--': np.nan}, inplace=True)
#Imprime para checar
print(df)
#Salva o arquivo em CSV
df.to_csv('teste.csv')


    


