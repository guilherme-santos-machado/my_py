import pandas as pd
import numpy as np
import os
import shutil

#Alteração da função para editar o header e coluna index
def movimentaArquivo(source, destination):
    if os.path.exists(destination):
        print('\nPasta /PNAD_2019 já existente.')
    else:
        os.makedirs(destination)   
        print('\npasta /PNAD_2019 criada.')
    files = os.listdir(source)
    for file in files:
        try: 
            extensao = file.split('.')[1]
            if extensao != 'git':
                shutil.move(f"{source}/{file}", destination)
            else:
                print('TA TENTANDO MOVER MEU .GIT?')
        except:
            print(file+' é uma pasta')
    


def listaParaEdicao(source):
    files = os.listdir(source)
    for file in files:
        try: 
            extensao = file.split('.')[1]
            if extensao != 'git':
                df = pd.read_csv(file, low_memory=False, header=1, index_col=1)
                df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                df = df.drop(columns=['7'])
                df.replace({'--': np.nan}, inplace=True)
                df.to_csv(file)
            else:
                print('------------- Pela regra, está tentando mover algum arquivo .git')
        except:
            print(file+'-----------Pela regra, esta tentando acessar ou alterar uma pasta (negado)')
    #Transferencia dos arquivos já tratados para uma pasta separada
    movimentaArquivo(source = './', destination = './tratado')


#Teste de edição em massa para planilhas com várias abas
source = "./download/"
files = os.listdir(source)
for file in files:
    try: 
        extensao = file.split('.')[1]
        if extensao != 'git':
            try:
                df = pd.ExcelFile(source+file)
                listaAbas = df.sheet_names
                for i in listaAbas:
                    df1 = pd.read_excel(df, sheet_name=i)
                    df1.drop(df1.head(7).index,inplace=True)    
                    df1.drop(df1.tail(2).index,inplace=True)
                    df1.to_csv(file+'_'+i+'.csv')
            except:
                print(file+' Sem autorização de acesso.')
        else:
            print('git encontrado')
    except:
        print('pasta encontrada')
  
    
listaParaEdicao(source = './')


