import wget
import os
import shutil
from datetime import date

#Variáveis
k = date.today()
anoInicial = 2012
thisYear = k.year
pdf = '.pdf'
txt = '.txt'
xls = '.xls'
pac = '.zip'
local = "./"
sucesso = 0
falho = 0

#Msgs
erro = '\nArquivo não disponível, favor verificar a FPT fo arquivo '

#Criação de função para download e tratamento de arquivos
def pegaETrataArquivo (url, file, end):  
    global sucesso  
    global falho
    try:
        wget.download(url)  
        shutil.move(file, end)      
        sucesso = sucesso + 1
        return sucesso
    except:
        print('\nDownload falhou '+ file)
        falho = falho + 1
        return falho


def criaContinuacao(link, tipo):
    file = 0
    for i in range (12):
        i = i + 1
        mes = f'{i}'
        for y in range (31):
            y = y + 1
            dia = f'{y}'
            if i<10:
                mes ='0' + f'{i}'                  
            else:
                mes = f'{i}'
            if y<10:
                dia = '0' + f'{y}' 
            else:
                dia = f'{y}'
            data = (f'{thisYear}' + mes + dia)
            try:
                wget.download(link + data + tipo)
                print('\nPegando arquivo')
                file = 1
                break
            except:
                print('\nArquivo não encontrado na data: ',data)
        if file == 1:
            break


def movimentaArquivo(local, destination):
    files = os.listdir(local)
    for file in files:
        try: 
            extensao = file.split('.')[1]
            if extensao != 'git':
                shutil.move(f"{local}/{file}", destination)
            else:
                print('TA TENTANDO MOVER MEU .GIT?')
        except:
            print(file+' é uma pasta')



#ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL



#Informações sobre os arquivos de Microdados, Pesquisas Suplementares Anuais e Histórico completo de atualizações

#Criando pasta do ano 2019
end = './PNAD_2019'
if os.path.exists(end):
    print('\nPasta /PNAD_2019 já existente.')
else:
    os.makedirs(end)   
    print('\npasta /PNAD_2019 criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/LEIA-ME.pdf','LEIA-ME.pdf', end )
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/PNADC_Pesquisas_Suplementares_Anuais_', pdf )
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/atualizacoes_divulgacao_anual_', txt)
movimentaArquivo(local, end)
end = ''

# Acumulados em determinada visita
#Criação da pasta Acumulados em determinada visita

end = './PNAD_2019/Acumulados em determinada visita'
if os.path.exists(end):
    print('\nPasta /Acumulados em determinada visita já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Acumulados em determinada visita criada.')

#Trata arquivos
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/LEIA-ME.pdf', 'LEIA-ME.pdf', end)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/PNADC_Pesquisas_Suplementares_Anuais_', pdf)
movimentaArquivo(local, end)
end = ''
#Geral - Acumulados em determinada visita

#Criação da pasta Geral
end = './PNAD_2019/Acumulados em determinada visita/Geral'
if os.path.exists(end):
    print('\nPasta /Geral já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Geral criada.')

#Trata arquivos
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Chaves_PNADC.pdf', 'Chaves_PNADC.pdf', end)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Definicao_variaveis_derivadas_PNADC_', pdf)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflacionamento_PNADC_anual_visita.txt', 'deflacionamento_PNADC_anual_visita.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2017.xls', 'deflator_PNADC_2017.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2018.xls', 'deflator_PNADC_2018.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2019.xls', 'deflator_PNADC_2019.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Estrutura_Atividade_CNAE_Domiciliar_2_0.xls', 'Estrutura_Atividade_CNAE_Domiciliar_2_0.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Estrutura_Ocupacao_COD.xls', 'Estrutura_Ocupacao_COD.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Grupamentos_ocupacionais_atividades_PNADC.pdf', 'Grupamentos_ocupacionais_atividades_PNADC.pdf', end)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/historico_temas_PNADC_anual_visita_', txt)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/PNADcIBGE_Deflator_Anual_Visita.pdf', 'PNADcIBGE_Deflator_Anual_Visita.pdf', end)
movimentaArquivo(local, end)
end = ''

#Acumulados em determinada visita

#Criação da pasta Visita 1
end = './PNAD_2019/Acumulados em determinada visita/Visita 1'
if os.path.exists(end):
    print('\nPasta /Visita 1 já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Visita 1 criada.')

end = ''
#Visita 1 - Dados

#Criação da pasta Visita 1 - Dados
end = './PNAD_2019/Acumulados em determinada visita/Visita 1/Dados'
if os.path.exists(end):
    print('\nPasta /Dados já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Dados criada.')

#Trata arquivos
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2012_visita1_20191016.zip', 'PNADC_2012_visita1_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2013_visita1_20191016.zip', 'PNADC_2013_visita1_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2014_visita1_20191016.zip', 'PNADC_2014_visita1_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2015_visita1_20191016.zip', 'PNADC_2015_visita1_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2016_visita1_20191016.zip', 'PNADC_2016_visita1_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2017_visita1_20191016.zip', 'PNADC_2017_visita1_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2018_visita1_20191218.zip', 'PNADC_2018_visita1_20191218.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2019_visita1.zip', 'PNADC_2019_visita1.zip', end)
movimentaArquivo(local, end)
end = ''
#Visita 1 - Documentação

#Criação da pasta Visita 1 - Documentação
end = './PNAD_2019/Acumulados em determinada visita/Visita 1/Documentação'
if os.path.exists(end):
    print('\nPasta /Documentação já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Documentação criada.')

#Trata arquivos
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2012_a_2014_visita1.xls', 'dicionario_PNADC_microdados_2012_a_2014_visita1.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2015_visita1.xls', 'dicionario_PNADC_microdados_2015_visita1.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2016_visita1.xls', 'dicionario_PNADC_microdados_2016_visita1.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2017_visita1.xls', 'dicionario_PNADC_microdados_2017_visita1.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2018_visita1.xls', 'dicionario_PNADC_microdados_2018_visita1.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2019_visita1.xls', 'dicionario_PNADC_microdados_2019_visita1.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2012_a_2014_visita1.txt', 'input_PNADC_2012_a_2014_visita1.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2015_visita1.txt', 'input_PNADC_2015_visita1.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2016_visita1.txt', 'input_PNADC_2016_visita1.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2017_visita1.txt', 'input_PNADC_2017_visita1.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2018_visita1.txt', 'input_PNADC_2018_visita1.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2019_visita1.txt', 'input_PNADC_2019_visita1.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/Observacoes_PNADC_2015_2016_visita1.pdf', 'Observacoes_PNADC_2015_2016_visita1.pdf', end)
movimentaArquivo(local, end)
end = '' 

#Visita 2

#Criação da pasta Visita 2
end = './PNAD_2019/Acumulados em determinada visita/Visita 2'
if os.path.exists(end):
    print('Pasta /Visita 2 já existente.')
else:
    os.makedirs(end)   
    print('pasta /Visita 2 criada.')

end = ''

#Criação da pasta Visita 2 - Dados
end = './PNAD_2019/Acumulados em determinada visita/Visita 2/Dados'
if os.path.exists(end):
    print('\nPasta /Visita 2/Dadosjá existente.')
else:
    os.makedirs(end)   
    print('\npasta /Visita 2/Dados criada.')

#Trata arquivos
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2016_visita5_20191016.zip', 'PNADC_2016_visita5_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2017_visita5_20191016.zip', 'PNADC_2017_visita5_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2018_visita5_20191016.zip', 'PNADC_2018_visita5_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2019_visita5_20191016.zip', 'PNADC_2019_visita5_20191016.zip', end)
movimentaArquivo(local, end)
end = ''

#Visita 2 - Documentação

#Criação da pasta Visita 2 - Documentação
end = './PNAD_2019/Acumulados em determinada visita/Visita 2/Documentação'
if os.path.exists(end):
    print('\nPasta /Visita 2/Documentação já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Visita 2/Documentação criada.')

#Trata dados
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/Observacoes_PNADC_2016_visita5.pdf', 'Observacoes_PNADC_2016_visita5.pdf', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2016_visita5.txt', 'input_PNADC_2016_visita5.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2017_visita5.txt', 'input_PNADC_2017_visita5.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2018_visita5.txt', 'input_PNADC_2018_visita5.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2019_visita5.txt', 'input_PNADC_2019_visita5.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2016_visita5.xls', 'dicionario_PNADC_microdados_2016_visita5.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2017_visita5.xls', 'dicionario_PNADC_microdados_2017_visita5.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2018_visita5.xls', 'dicionario_PNADC_microdados_2018_visita5.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2019_visita5.xls', 'dicionario_PNADC_microdados_2019_visita5.xls', end)
movimentaArquivo(local, end)
end = ''


#Visita 5

#Criação da pasta Visita 5
end = './PNAD_2019/Acumulados em determinada visita/Visita 5'
if os.path.exists(end):
    print('\nPasta /Visita 5 já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Visita 5 criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/LEIA-ME.pdf', 'LEIA-ME.pdf', end)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/PNADC_Pesquisas_Suplementares_Anuais_', pdf)
movimentaArquivo(local, end)
end = ''

#Criação da pasta Visita 5 - Dados
end = './PNAD_2019/Acumulados em determinada visita/Visita 5/Dados'
if os.path.exists(end):
    print('\nPasta /Visita 5/Dados já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Visita 5/Dados criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2019_visita5.zip', 'PNADC_2019_visita5.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2018_visita5_20191016.zip', 'PNADC_2018_visita5_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2017_visita5_20191016.zip', 'PNADC_2017_visita5_20191016.zip', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2016_visita5_20191016.zip', 'PNADC_2016_visita5_20191016.zip', end)
movimentaArquivo(local, end)
end = ''


#Criação da pasta Visita 5 - Documentação
end = './PNAD_2019/Acumulados em determinada visita/Visita 5/Documentação'
if os.path.exists(end):
    print('\nPasta /Visita 5/Documentação já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Visita 5/Documentação criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/Observacoes_PNADC_2016_visita5.pdf', 'Observacoes_PNADC_2016_visita5.pdf', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2016_visita5.txt', 'input_PNADC_2016_visita5.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2017_visita5.txt', 'input_PNADC_2017_visita5.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2018_visita5.txt', 'input_PNADC_2018_visita5.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2019_visita5.txt', 'input_PNADC_2019_visita5.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2016_visita5.xls', 'dicionario_PNADC_microdados_2016_visita5.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2017_visita5.xls', 'dicionario_PNADC_microdados_2017_visita5.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2018_visita5.xls', 'dicionario_PNADC_microdados_2018_visita5.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2019_visita5.xls', 'dicionario_PNADC_microdados_2019_visita5.xls', end)
movimentaArquivo(local, end)
end = ''



#TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL 



#Concentrados em determinado trimestre

#Criação da pasta Acumulados em determinada visita
end = './PNAD_2019/Concentrados em determinado trimestre'
if os.path.exists(end):
    print('\nPasta /Concentrados em determinado trimestre já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Concentrados em determinado trimestre criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/LEIA-ME.pdf', 'LEIA-ME.pdf', end)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/PNADC_Pesquisas_Suplementares_Anuais_', pdf)
movimentaArquivo(local, end)
end = ''


#Geral

#Criação da pasta Geral
end = './PNAD_2019/Concentrados em determinado trimestre/Geral'
if os.path.exists(end):
    print('\nPasta /Concentrados em determinado trimestre/Geral já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Concentrados em determinado trimestre/Geral criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/PNADcIBGE_Deflator_Anual_Trimestre.pdf', 'PNADcIBGE_Deflator_Anual_Trimestre.pdf', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Grupamentos_ocupacionais_atividades_PNADC.pdf', 'Grupamentos_ocupacionais_atividades_PNADC.pdf', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Estrutura_Ocupacao_COD.xls', 'Estrutura_Ocupacao_COD.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Estrutura_Atividade_CNAE_Domiciliar_2_0.xls', 'Estrutura_Atividade_CNAE_Domiciliar_2_0.xls', end)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Definicao_variaveis_derivadas_PNADC_', pdf)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Chaves_PNADC.pdf', 'Chaves_PNADC.pdf', end)
movimentaArquivo(local, end)
end = ''

#Concentrados em determinado trimestre

#Criação da pasta Trimestre 1
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 1'
if os.path.exists(end):
    print('\nPasta /Trimestre 1 já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 1 criada.')

end = ''


#Trimestre 1 - Dados

#Criação da pasta Dados
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 1/Dados'
if os.path.exists(end):
    print('\nPasta /Trimestre 1/Dados já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 1/Dados criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_1/Dados/informacao_importante_anual_trimestre1.txt', 'informacao_importante_anual_trimestre1.txt', end)
movimentaArquivo(local, end)
end = ''


#Trimestre 1 - Documentação

#Criação da pasta Documentação
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 1/Documentação'
if os.path.exists(end):
    print('\nPasta /Trimestre 1/Documentação já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 1/Documentação criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_1/Documentacao/informacao_importante_anual_trimestre1.txt', 'informacao_importante_anual_trimestre1.txt', end)
movimentaArquivo(local, end)
end = ''


#Trimestre 2 - Dados

#Criação da pasta Dados
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 2/Dados'
if os.path.exists(end):
    print('\nPasta /Trimestre 2/Dados já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 2/Dados criada.')

#Trata arquivo
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2016_trimestre2_', pac)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2017_trimestre2_', pac)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2018_trimestre2_', pac)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2019_trimestre2_', pac)
movimentaArquivo(local, end)
end = ''

#Trimestre 2 - Documentação

#Criação da pasta Documentação
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 2/Documentação'
if os.path.exists(end):
    print('\nPasta /Trimestre 2/Documentação já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 2/Documentação criada.')

#Trata arquivo
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/input_PNADC_trimestre2_', txt)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/dicionario_PNADC_microdados_trimestre2_', xls)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2019_trimestre2_', xls)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2018_trimestre2_', xls)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2017_trimestre2_', xls)
movimentaArquivo(local, end)
end = ''


#Trimestre 3 - Dados

#Criação da pasta Dados
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 3/Dados'
if os.path.exists(end):
    print('\nPasta /Trimestre 3/Dados já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 3/Dados criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Dados/PNADC_2019_trimestre3.zip', 'PNADC_2019_trimestre3.zip', end)
movimentaArquivo(local, end)
end = ''


#Trimestre 3 - Documentação

#Criação da pasta Documentação
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 3/Documentação'
if os.path.exists(end):
    print('\nPasta /Trimestre 3/Documentação já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 3/Documentação criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/input_PNADC_trimestre3.txt', 'input_PNADC_trimestre3.txt', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/dicionario_PNADC_microdados_trimestre3.xls', 'dicionario_PNADC_microdados_trimestre3.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/deflator_PNADC_2019_trimestre3.xls', 'deflator_PNADC_2019_trimestre3.xls', end)
movimentaArquivo(local, end)
end = ''


#Trimestre 4 - Dados

#Criação da pasta Dados
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 4/Dados'
if os.path.exists(end):
    print('\nPasta /Trimestre 4/Dados já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 4/Dados criada.')

#Trata arquivo
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2016_trimestre4_', pac)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2017_trimestre4_', pac)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2018_trimestre4.zip', 'PNADC_2018_trimestre4.zip', end)
movimentaArquivo(local, end)
end = ''


#Trimestre 4 - Documentação

#Criação da pasta Documentação
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 4/Documentação'
if os.path.exists(end):
    print('\nPasta /Trimestre 4/Documentação já existente.')
else:
    os.makedirs(end)   
    print('\npasta /Trimestre 4/Documentação criada.')

#Trata arquivo
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/deflator_PNADC_2017_trimestre4.xls', 'deflator_PNADC_2017_trimestre4.xls', end)
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/deflator_PNADC_2018_trimestre4.xls', 'deflator_PNADC_2018_trimestre4.xls', end)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/dicionario_PNADC_microdados_trimestre4_', xls)
criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/input_PNADC_trimestre4_', txt)
movimentaArquivo(local, end)
end = ''



print('\nTotal: ',falho+sucesso)
print('\nSucesso de download: ', sucesso)
print('\nFalha de download: ', falho)
print('\nBOOM SHAKALAKA!')
