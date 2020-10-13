import pandas as pd
import numpy as np
import os
import shutil
#Alteração da função para editar o header e coluna index
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

#Função Banco Brasil
def brasil(file, coluna_valor, fileName):
    df = pd.read_excel(file, header=1)
    brasil = df.loc[df['UNIDGEO'] == coluna_valor]
    brasil.to_csv(fileName+'_'+coluna_valor+'.csv')
    movimentaArquivo(source = './', destination = './brasil')
#Função Banco Região
def regiao(file, coluna_valor, fileName):
    df = pd.read_excel(file, header=1)
    brasil = df.loc[df['UNIDGEO'] == coluna_valor]
    brasil.to_csv(fileName+'_'+coluna_valor+'.csv')
    movimentaArquivo(source = './', destination = './regional')
#Função Banco UFS
def uf(file, coluna_valor, fileName):
    df = pd.read_excel(file, header=1)
    brasil = df.loc[df['UNIDGEO'] == coluna_valor]
    brasil.to_csv(fileName+'_'+coluna_valor+'.csv')
    movimentaArquivo(source = './', destination = './ufs')


def listaParaEdicao(source):
    files = os.listdir(source)
    for file in files:
        try: 
            extensao = file.split('.')[1]
            nameFile = file.split('.')[0]
            if extensao != 'git':
                try:
                    df = pd.read_csv(file, header=1)
                    # df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
                    # df = df.drop(columns=['7'])
                    df.replace({'--': np.nan}, inplace=True)
                    # df.to_csv(nameFile+'.csv')
                    #Banco brasil
                    brasil('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'brasil', nameFile)


                    #banco Região
                    #norte
                    regiao('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Norte', nameFile)
                    #nordeste
                    regiao('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Nordeste', nameFile)
                    #sul
                    regiao('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Sul', nameFile)
                    #sudeste
                    regiao('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Sudeste', nameFile)
                    #centro
                    regiao('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Centro-Oeste', nameFile)


                    #banco UF
                    # Rondônia
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Rondônia', nameFile)
                    # Acre
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Acre', nameFile)
                    # Amazonas
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Amazonas', nameFile)
                    # Roraima
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Roraima', nameFile)
                    # Pará
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Pará', nameFile)
                    # Amapá
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Amapá', nameFile)
                    # Tocantins
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Tocantins', nameFile)
                    # Maranhão
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Maranhão', nameFile)
                    # Piauí
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Piauí', nameFile)
                    # Ceará
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Ceará', nameFile)
                    # Rio Grande do Norte
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Rio Grande do Norte', nameFile)
                    # Paraíba
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Paraíba', nameFile)
                    # Pernambuco
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Pernambuco', nameFile)
                    # Alagoas
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Alagoas', nameFile)
                    # Sergipe
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Sergipe', nameFile)
                    # Bahia
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Bahia', nameFile)
                    # Minas Gerais
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Minas Gerais', nameFile)
                    # Espírito Santo
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Espírito Santo', nameFile)
                    # Rio de Janeiro
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Rio de Janeiro', nameFile)
                    # São Paulo
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'São Paulo', nameFile)
                    # Paraná
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Paraná', nameFile)
                    # Santa Catarina
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Santa Catarina', nameFile)
                    # Rio Grande do Sul
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Rio Grande do Sul', nameFile)
                    # Mato Grosso do Sul
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Mato Grosso do Sul', nameFile)
                    # Mato Grosso
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Mato Grosso', nameFile)
                    # Goiás
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Goiás', nameFile)
                    # Distrito Federal
                    uf('ATU_BRASIL_REGIOES_UFS_2019.xlsx', 'Distrito Federal', nameFile)
                except:
                    print('Erro ao editar '+file)
            else:
                print('------------- Pela regra, está tentando mover algum arquivo .git')
        except:
            print(file+'-----------Pela regra, esta tentando acessar ou alterar uma pasta (negado)')
    #Transferencia dos arquivos já tratados para uma pasta separada
    


#Teste de edição em massa para planilhas com várias abas
source = "./download/"
files = os.listdir(source)
for file in files:
    try: 
        extensao = file.split('.')[1]
        nameFile = file.split('.')[0]
        if extensao != 'git':
            try:
                df = pd.ExcelFile(source+file)
                listaAbas = df.sheet_names
                for i in listaAbas:
                    df1 = pd.read_excel(df, sheet_name=i)
                    df1.drop(df1.head(7).index,inplace=True)    
                    df1.drop(df1.tail(2).index,inplace=True)
                    df1.to_csv(i+'_'+nameFile+'.csv')
            except:
                print(file+' Sem autorização de acesso.')
        else:
            print('git encontrado')
    except:
        print('pasta encontrada')
  
    
listaParaEdicao(source = './')

# source = './'
# files = os.listdir(source)
# for file in files:
#     extensao = file.split('.')[0]
#     if extensao == 'download':
#         shutil.rmtree(source+file, ignore_errors=True)
#     else:
#         print(file+' não foi apagado.')


