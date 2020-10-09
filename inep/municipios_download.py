import wget
import os
import shutil

#Criação de função para download e movimentação de arquivos
def pegaETrataArquivo (lista):  
    for item in lista:
        try:
            wget.download(item)      

        except:
            print('\nDownload falhou '+ item)

def movimentaArquivo(source, destination):
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

#Cria a pasta de Download caso não tenha
destination = './download'
if os.path.exists(destination):
    print('\nPasta /Download já existente.')
else:
    os.makedirs(destination)   
    print('\npasta /Download criada.')

#Download de bases de Escolas 2007 - 2019 - Média de Alunos por Turma
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Média de Horas-Aula diária
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Taxas de distorção idade-série
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Taxas de Rendimento
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Taxa de Não Resposta (TNR)
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Percentual de Docentes com Curso Superior
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Adequação da Formação Docente
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Regularidade do Corpo Docente
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Esforço Docente
pegaETrataArquivo(lista=[])

#Download de bases de Escolas 2007 - 2019 - Complexidade de Gestão da Escola
pegaETrataArquivo(lista=[])


#Download de bases de Escolas 2007 - 2019 - Nível Socioeconômico
pegaETrataArquivo(lista=[])

#Move arquivos para a pasta de Download
movimentaArquivo(source='./', destination='./download')


#Download de bases de Escolas 2007 - 2019 - Taxas de Transição
#Download de bases de Escolas 2007 - 2019 - Remuneração Média dos Docentes
#Download de bases de Escolas 2007 - 2019 - Indicador de Fluxo da Educação Superior


# import extrai_limpa_zip
# import retira_pasta