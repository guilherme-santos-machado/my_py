import wget
import os
import shutil
from datetime import date

#Variáveis
k = date.today()
anoInicial = 2007
thisYear = k.year
dif = thisYear- anoInicial
end = './indicadores/'
base = './'

def download(brasil, municipios, escolas, ano):
    try:
        wget.download(brasil)
    except:
        print('Falha no download do arquivo Brasil do ano: '+f'{ano}')
    try:
        wget.download(municipios)
    except:
        print('Falha no download do arquivo Municípios do ano: '+f'{ano}')
    try:
        wget.download(escolas)
    except:
        print('Falha no download do arquivo Escolas do ano: '+f'{ano}')

#Cria pasta do projeto
if os.path.exists(end):
    print('\nPasta do ano.',end, ' já existe!')
else:
    os.makedirs(end)   
    print('\nPasta do ano.',end, ' criada!')

for i in range (dif):
#    i += 1
    ano = anoInicial + i
    #Cria pasta do ano
    caminho = end+f'{ano}'
    if os.path.exists(caminho):
        print('\nPasta do ano.',caminho, ' já existe!')
    else:
        os.makedirs(caminho)   
        print('\nPasta do ano.',caminho, ' criada!')



    if ano < 2010:
        brasil = 'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/'+f'{ano}'+'/media_alunos_turma_brasil_regioes_ufs_'+f'{ano}'+'.zip'
        municipios = 'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/'+f'{ano}'+'/media_alunos_turma_municipios_'+f'{ano}'+'.zip'
        escolas = 'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/'+f'{ano}'+'/media_alunos_turma_escolas_'+f'{ano}'+'.zip'
        
        download(brasil, municipios, escolas, ano)
        if ano == 2010:
            brasil = 'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/'+f'{ano}'+'/media_alunos_turma_brasil_regioes_ufs_'+f'{ano}'+'_3.zip'
            municipios = 'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/'+f'{ano}'+'/media_alunos_turma_municipios_'+f'{ano}'+'_3.zip'
            escolas= 'http://download.inep.gov.br/informacoes_estatisticas/2011/indicadores_educacionais/media_alunos_turma/'+f'{ano}'+'/media_alunos_turma_escolas_'+f'{ano}'+'_3.zip'
            download(brasil, municipios, escolas, ano)
            if ano == 2011:
                brasil = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/alunos_turma/alunos_turma_brasil_regioes_UFs_'+f'{ano}'+'.zip'
                municipios = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/alunos_turma/alunos_turma_municipios_'+f'{ano}'+'.zip'
                escolas = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/alunos_turma/alunos_turma_escolas_'+f'{ano}'+'.zip'
                download(brasil, municipios, escolas, ano)
                if ano < 2016:
                    brasil = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/alunos_turma/media_alunos_turma_brasil_regioes_UFs_'+f'{ano}'+'.zip'
                    municipios = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/alunos_turma/media_alunos_turma_municipios_'+f'{ano}'+'.zip'
                    escolas = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/alunos_turma/media_alunos_turma_escolas_'+f'{ano}'+'.zip'
                    download(brasil, municipios, escolas, ano)
    else:
        brasil = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/ATU_'+f'{ano}'+'_BRASIL_REGIOES_UFS.zip'
        municipios = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/ATU_'+f'{ano}'+'_MUNICIPIOS.zip'
        escolas = 'http://download.inep.gov.br/informacoes_estatisticas/indicadores_educacionais/'+f'{ano}'+'/ATU_'+f'{ano}'+'_ESCOLAS.zip'
        download(brasil, municipios, escolas, ano)


    print('Fim do download do ano: '+f'{ano}')
    files = os.listdir('./')
    for file in files:
        try: 
            extensao = file.split('.')[1]
            if extensao != 'git':
                shutil.move(f"{base}/{file}", caminho)
            else:
                print('TA TENTANDO MOVER MEU .GIT?')
        except:
            print(file+' é uma pasta')

