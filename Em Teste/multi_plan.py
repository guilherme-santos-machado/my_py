import pandas as pd
import numpy as np
import os

#Alteração da função para editar o header e coluna index
def listaParaEdicao(source):
    files = os.listdir(source)
    for file in files:
        try: 
            extensao = file.split('.')[1]
            if extensao != 'git':
                df = pd.read_csv(file, low_memory=False, header=1, index_col=1)
                df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df.replace({'--': np.nan}, inplace=True)
                print(df)
                df.to_csv(file)
            else:
                print('------------- Pela regra, está tentando mover algum arquivo .git')
        except:
            print('-----------Pela regra, esta tentando acessar ou alterar uma pasta (negado)')


#Teste de edição em massa para planilhas com várias abas
source = "./"
files = os.listdir(source)
for file in files:
    try: 
        extensao = file.split('.')[1]
        if extensao != 'git':
            df = pd.ExcelFile(file)
            listaAbas = df.sheet_names
            for i in listaAbas:
                df1 = pd.read_excel(df, sheet_name=i)
                df1.drop(df1.head(4).index,inplace=True)    
                df1.drop(df1.tail(2).index,inplace=True)
                df1.to_csv(i+'.csv')
        else:
            print('git encontrado')
    except:
        print('pasta encontrada')
  
    
listaParaEdicao(source)


