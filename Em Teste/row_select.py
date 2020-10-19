import pandas as pd 
import os
import shutil
import numpy as np

#Função Banco Brasil
# def brasil(file, coluna_valor, nameFile):
#     df = pd.read_csv(file)
#     brasil = df.loc[df['SG_UF'] == coluna_valor]
#     print(brasil)
    # arquivo = nameFile+'_'+coluna_valor+'.csv'
    # brasil.to_csv(arquivo)
    # shutil.move(arquivo, './brasil')
#Função Banco Região
# def regiao(file, coluna_valor, nameFile):
#     df = pd.read_csv(file)
#     brasil = df.loc[df['SG_UF'] == coluna_valor]
#     arquivo = nameFile+'_'+coluna_valor+'.csv'
#     brasil.to_csv(arquivo)
#     shutil.move(arquivo, './regiao')
# #Função Banco UFS
# def uf(file, coluna_valor, nameFile):
#     df = pd.read_csv(file)
#     brasil = df.loc[df['SG_UF'] == coluna_valor]
#     arquivo = nameFile+'_'+coluna_valor+'.csv'
#     brasil.to_csv(arquivo)
#     shutil.move(arquivo, './uf')


# #Editando na pasta de Download
# source = "./download/"
# files = os.listdir(source)
# for file in files:
#     try: 
#         extensao = file.split('.')[1]
#         nameFile = file.split('.')[0]
#         if extensao != 'git':
#             try:
#                 df = pd.ExcelFile(source+file)
#                 listaAbas = df.sheet_names
#                 for i in listaAbas:
#                     df1 = pd.read_excel(df, sheet_name=i, header = 8)
                                           
#                     df1.drop(df1.head(7).index,inplace=True)    
#                     df1.drop(df1.tail(2).index,inplace=True)
#                     df1.replace({'--': np.nan}, inplace=True)
#                     df1.to_csv('download/'+nameFile+'.csv')
#             except:
#                 print(file+' Sem autorização de acesso.')
#         else:
#             print('git encontrado')
#     except:
#         print('pasta encontrada')  

#####Correto até aqui#####


#TRATA A PLANILHA E SALVA FORA DA PASTA DE DOWNLOAD
# files = os.listdir(source)
# for file in files:
#     extensao = file.split('.')[1]
#     nameFile = file.split('.')[0]
#     if extensao == 'csv':
#         df = pd.read_csv(source+file, index_col=1)
#         df = df.loc[:, ~df.columns.str.contains('^Unnamed: 0')]          
#         df.to_csv(file)


source = './'
files = os.listdir(source)
for file in files:
    try:
        df = pd.read_csv(file)
        df1 = df.loc[df['UNIDGEO'] == 'Brasil']
        df1.to_csv('Brasil__'+file)
    except:
        print(file+' acesso negado!')




        # df = pd.read_csv(file, index_col=1)
        # brasil = df.loc[df['SG_UF'] == 'Brasil']
        # arquivo = nameFile+'_'+'brasil.csv'
        # brasil.to_csv(arquivo)


#Trata a base e envia para a respectiva pasta
# files = os.listdir(source)
# for file in files:
#     extensao = file.split('.')[1]
#     nameFile = file.split('.')[0]
#     try: 
#         if extensao == 'csv':
#             #Banco brasil
#             brasil(file, 'Brasil', nameFile)
#             #banco Região
#             #norte
#             regiao(file, 'Norte', nameFile)
#             #nordeste
#             regiao(file, 'Nordeste', nameFile)
#             #sul
#             regiao(file, 'Sul', nameFile)
#             #sudeste
#             regiao(file, 'Sudeste', nameFile)
#             #centro
#             regiao(file, 'Centro-Oeste', nameFile)
#             #banco UF
#             # Rondônia
#             uf(file, 'Rondônia', nameFile)
#             # Acre
#             uf(file, 'Acre', nameFile)
#             # Amazonas
#             uf(file, 'Amazonas', nameFile)
#             # Roraima
#             uf(file, 'Roraima', nameFile)
#             # Pará
#             uf(file, 'Pará', nameFile)
#             # Amapá
#             uf(file, 'Amapá', nameFile)
#             # Tocantins
#             uf(file, 'Tocantins', nameFile)
#             # Maranhão
#             uf(file, 'Maranhão', nameFile)
#             # Piauí
#             uf(file, 'Piauí', nameFile)
#             # Ceará
#             uf(file, 'Ceará', nameFile)
#             # Rio Grande do Norte
#             uf(file, 'Rio Grande do Norte', nameFile)
#             # Paraíba
#             uf(file, 'Paraíba', nameFile)
#             # Pernambuco
#             uf(file, 'Pernambuco', nameFile)
#             # Alagoas
#             uf(file, 'Alagoas', nameFile)
#             # Sergipe
#             uf(file, 'Sergipe', nameFile)
#             # Bahia
#             uf(file, 'Bahia', nameFile)
#             # Minas Gerais
#             uf(file, 'Minas Gerais', nameFile)
#             # Espírito Santo
#             uf(file, 'Espírito Santo', nameFile)
#             # Rio de Janeiro
#             uf(file, 'Rio de Janeiro', nameFile)
#             # São Paulo
#             uf(file, 'São Paulo', nameFile)
#             # Paraná
#             uf(file, 'Paraná', nameFile)
#             # Santa Catarina
#             uf(file, 'Santa Catarina', nameFile)
#             # Rio Grande do Sul
#             uf(file, 'Rio Grande do Sul', nameFile)
#             # Mato Grosso do Sul
#             uf(file, 'Mato Grosso do Sul', nameFile)
#             # Mato Grosso
#             uf(file, 'Mato Grosso', nameFile)
#             # Goiás
#             uf(file, 'Goiás', nameFile)
#             # Distrito Federal
#             uf(file, 'Distrito Federal', nameFile)
#     except:
#         print(nameFile+' Não deu acesso')
