#Importação de bibliotecas
import pandas as pd
import numpy as np
import os
import shutil

###FUNÇÕES###
#movimentaArquivo - Pega os arquivos a origem padrão "./" e joga para uma pasta de destino.
def movimentaArquivo(source, destination):
    if os.path.exists(destination):
        print('\nPasta '+destination)
    else:
        os.makedirs(destination)   
        print('\npasta '+destination)
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
    
#listaParaEdicao - Lista os arquivos de um local, apaga colunas com Unnamed, set "--" para "null"
def listaParaEdicao(source):
    files = os.listdir(source)
    for file in files:
        try: 
            extensao = file.split('.')[1]
            nameFile = file.split('.')[0]
            #Ignora o arquivo com extesão .git - Arquivo base do projeto para o GITHUB
            if extensao != 'git':
                try:
                    df = pd.read_csv(file, low_memory=False,header=1, index_col=1)
                    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                    df = df.drop(columns=['7'])
                    df.replace({'--': np.nan}, inplace=True)
                    df.to_csv(nameFile+'.csv')
                except:
                    print('Erro ao editar '+file)
            else:
                print('------------- Pela regra, está tentando mover algum arquivo .git')
        except:
            print(file+'-----------Pela regra, esta tentando acessar ou alterar uma pasta (negado)')
    #Transferencia dos arquivos já tratados para uma pasta separada
    movimentaArquivo(source = './', destination = './brasil regioes ufs')


#Início do tratamento em Lista de um local
#Definição do local
source = "./download/"
#Criação de LISTA com os arquivos do local
files = os.listdir(source)
for file in files:
    try: 
        extensao = file.split('.')[1]
        nameFile = file.split('.')[0]
        if extensao != 'git':
            try:
                #Cria lista com as abas do arquivo
                df = pd.ExcelFile(source+file)
                listaAbas = df.sheet_names
                for i in listaAbas:
                    #Deleta as 7 primeiras linhas e as duas últimas
                    df1 = pd.read_excel(df, sheet_name=i)
                    df1.drop(df1.head(7).index,inplace=True)    
                    df1.drop(df1.tail(2).index,inplace=True)
                    df1.to_csv(nameFile+'.csv')
            except:
                print(file+' Sem autorização de acesso.')
        else:
            print('git encontrado')
    except:
        print('pasta encontrada')
  
    
listaParaEdicao(source = './')

#Lisra a pasta raiz do projeto
source = './'
files = os.listdir(source)
#Apaga a pasta "Download" e todos os arquivos não tratados, ignorando qualquer tipo de erro
for file in files:
    extensao = file.split('.')[0]
    if extensao == 'download':
        shutil.rmtree(source+file, ignore_errors=True)
    else:
        print(file+' não foi apagado.')


