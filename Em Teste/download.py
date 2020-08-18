import wget
import os
import shutil
erro = '\nArquivo não disponível, favor verificar a FPT fo arquivo '
sucesso = 0
falho = 0

#Criação de função para download e tratamento de arquivos
def pegaETrataArquivo (url, file, end):    
    try:
        wget.download(url)  
        shutil.move(file, end)      
        sucesso =+ 1
        return sucesso
    except:
        print('Download falhou '+ file)
        falho =+ 1
        return falho



#ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL



#Informações sobre os arquivos de Microdados, Pesquisas Suplementares Anuais e Histórico completo de atualizações

#Criando pasta do ano 2019
end = './PNAD_2019'
if os.path.exists(end):
    print('Pasta /PNAD_2019 já existente.')
else:
    os.makedirs(end)   
    print('pasta /PNAD_2019 criada.')

pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/LEIA-ME.pdf','LEIA-ME.pdf', end )
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf', 'PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf', end )
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/atualizacoes_divulgacao_anual_20200716.txt', 'atualizacoes_divulgacao_anual_20200716.txt', end)
end = ''

# Acumulados em determinada visita
#Criação da pasta Acumulados em determinada visita

end = './PNAD_2019/Acumulados em determinada visita'
if os.path.exists(end):
    print('Pasta /Acumulados em determinada visita já existente.')
else:
    os.makedirs(end)   
    print('pasta /Acumulados em determinada visita criada.')

#Trata arquivos
pegaETrataArquivo('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/LEIA-ME.pdf', 'LEIA-ME.pdf', end)
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf')
    shutil.move('PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf')
    falho = falho + 1

end = ''
#Geral - Acumulados em determinada visita

#Criação da pasta Geral
end = './PNAD_2019/Acumulados em determinada visita/Geral'
if os.path.exists(end):
    print('Pasta /Geral já existente.')
else:
    os.makedirs(end)   
    print('pasta /Geral criada.')

#Trata arquivos
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Chaves_PNADC.pdf')
    shutil.move('Chaves_PNADC.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Chaves_PNADC.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Definicao_variaveis_derivadas_PNADC_20200211.pdf')
    shutil.move('Definicao_variaveis_derivadas_PNADC_20200211.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Definicao_variaveis_derivadas_PNADC_20200211.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflacionamento_PNADC_anual_visita.txt')
    shutil.move('deflacionamento_PNADC_anual_visita.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflacionamento_PNADC_anual_visita.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2017.xls')
    shutil.move('deflator_PNADC_2017.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2017.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2018.xls')
    shutil.move('deflator_PNADC_2018.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2018.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2019.xls')
    shutil.move('deflator_PNADC_2019.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2019.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Estrutura_Atividade_CNAE_Domiciliar_2_0.xls')
    shutil.move('Estrutura_Atividade_CNAE_Domiciliar_2_0.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'Estrutura_Atividade_CNAE_Domiciliar_2_0.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Estrutura_Ocupacao_COD.xls')
    shutil.move('Estrutura_Ocupacao_COD.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'Estrutura_Ocupacao_COD.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Grupamentos_ocupacionais_atividades_PNADC.pdf')
    shutil.move('Grupamentos_ocupacionais_atividades_PNADC.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Grupamentos_ocupacionais_atividades_PNADC.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/historico_temas_PNADC_anual_visita_20200506.txt')
    shutil.move('historico_temas_PNADC_anual_visita_20200506.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'historico_temas_PNADC_anual_visita_20200506.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/PNADcIBGE_Deflator_Anual_Visita.pdf')
    shutil.move('PNADcIBGE_Deflator_Anual_Visita.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADcIBGE_Deflator_Anual_Visita.pdf')
    falho = falho + 1

end = ''
#Acumulados em determinada visita

#Criação da pasta Visita 1
end = './PNAD_2019/Acumulados em determinada visita/Visita 1'
if os.path.exists(end):
    print('Pasta /Visita 1 já existente.')
else:
    os.makedirs(end)   
    print('pasta /Visita 1 criada.')

end = ''
#Visita 1 - Dados

#Criação da pasta Visita 1 - Dados
end = './PNAD_2019/Acumulados em determinada visita/Visita 1/Dados'
if os.path.exists(end):
    print('Pasta /Dados já existente.')
else:
    os.makedirs(end)   
    print('pasta /Dados criada.')

#Trata arquivos
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2012_visita1_20191016.zip')
    shutil.move('PNADC_2012_visita1_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2012_visita1_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2013_visita1_20191016.zip')
    shutil.move('PNADC_2013_visita1_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2013_visita1_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2014_visita1_20191016.zip')
    shutil.move('PNADC_2014_visita1_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2014_visita1_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2015_visita1_20191016.zip')
    shutil.move('PNADC_2015_visita1_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2015_visita1_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2016_visita1_20191016.zip')
    shutil.move('PNADC_2016_visita1_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2016_visita1_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2017_visita1_20191016.zip')
    shutil.move('PNADC_2017_visita1_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2017_visita1_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2018_visita1_20191218.zip')
    shutil.move('PNADC_2018_visita1_20191218.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2018_visita1_20191218.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2019_visita1.zip')
    shutil.move('PNADC_2019_visita1.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2019_visita1.zip')
    falho = falho + 1

end = ''
#Visita 1 - Documentação

#Criação da pasta Visita 1 - Documentação
end = './PNAD_2019/Acumulados em determinada visita/Visita 1/Documentação'
if os.path.exists(end):
    print('Pasta /Documentação já existente.')
else:
    os.makedirs(end)   
    print('pasta /Documentação criada.')

#Trata arquivos
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2012_a_2014_visita1.xls')
    shutil.move('dicionario_PNADC_microdados_2012_a_2014_visita1.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2012_a_2014_visita1.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2015_visita1.xls')
    shutil.move('dicionario_PNADC_microdados_2015_visita1.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2015_visita1.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2016_visita1.xls')
    shutil.move('dicionario_PNADC_microdados_2016_visita1.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2016_visita1.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2017_visita1.xls')
    shutil.move('dicionario_PNADC_microdados_2017_visita1.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2017_visita1.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2018_visita1.xls')
    shutil.move('dicionario_PNADC_microdados_2018_visita1.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2018_visita1.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2019_visita1.xls')
    shutil.move('dicionario_PNADC_microdados_2019_visita1.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2019_visita1.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2012_a_2014_visita1.txt')
    shutil.move('input_PNADC_2012_a_2014_visita1.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2012_a_2014_visita1.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2015_visita1.txt')
    shutil.move('input_PNADC_2015_visita1.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2015_visita1.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2016_visita1.txt')
    shutil.move('input_PNADC_2016_visita1.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2016_visita1.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2017_visita1.txt')
    shutil.move('input_PNADC_2017_visita1.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2017_visita1.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2018_visita1.txt')
    shutil.move('input_PNADC_2018_visita1.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2018_visita1.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2019_visita1.txt')
    shutil.move('input_PNADC_2019_visita1.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2019_visita1.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/Observacoes_PNADC_2015_2016_visita1.pdf')
    shutil.move('Observacoes_PNADC_2015_2016_visita1.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Observacoes_PNADC_2015_2016_visita1.pdf')
    falho = falho + 1

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
    print('Pasta /Visita 2/Dadosjá existente.')
else:
    os.makedirs(end)   
    print('pasta /Visita 2/Dados criada.')

#Trata arquivos
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2016_visita5_20191016.zip')
    shutil.move('PNADC_2016_visita5_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2016_visita5_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2017_visita5_20191016.zip')
    shutil.move('PNADC_2017_visita5_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2017_visita5_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2018_visita5_20191016.zip')
    shutil.move('PNADC_2018_visita5_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2018_visita5_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2019_visita5_20191016.zip')
    shutil.move('PNADC_2019_visita5_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2019_visita5_20191016.zip')
    falho = falho + 1

end = ''
#Visita 2 - Documentação

#Criação da pasta Visita 2 - Documentação
end = './PNAD_2019/Acumulados em determinada visita/Visita 2/Documentação'
if os.path.exists(end):
    print('Pasta /Visita 2/Documentação já existente.')
else:
    os.makedirs(end)   
    print('pasta /Visita 2/Documentação criada.')

#Trata dados
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/Observacoes_PNADC_2016_visita5.pdf')
    shutil.move('Observacoes_PNADC_2016_visita5.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Observacoes_PNADC_2016_visita5.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2016_visita5.txt')
    shutil.move('input_PNADC_2016_visita5.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2016_visita5.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2017_visita5.txt')
    shutil.move('input_PNADC_2017_visita5.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2017_visita5.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2018_visita5.txt')
    shutil.move('input_PNADC_2018_visita5.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2018_visita5.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2019_visita5.txt')
    shutil.move('input_PNADC_2019_visita5.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2019_visita5.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2016_visita5.xls')
    shutil.move('dicionario_PNADC_microdados_2016_visita5.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2016_visita5.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2017_visita5.xls')
    shutil.move('dicionario_PNADC_microdados_2017_visita5.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2017_visita5.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2018_visita5.xls')
    shutil.move('dicionario_PNADC_microdados_2018_visita5.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2018_visita5.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2019_visita5.xls')
    shutil.move('dicionario_PNADC_microdados_2019_visita5.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2019_visita5.xls')
    falho = falho + 1

end = ''


#Visita 5

#Criação da pasta Visita 5
end = './PNAD_2019/Acumulados em determinada visita/Visita 5'
if os.path.exists(end):
    print('Pasta /Visita 5 já existente.')
else:
    os.makedirs(end)   
    print('pasta /Visita 5 criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/LEIA-ME.pdf')
    shutil.move('LEIA-ME.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'LEIA-ME.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf')
    shutil.move('PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf')
    falho = falho + 1
end = ''


#Criação da pasta Visita 5 - Dados
end = './PNAD_2019/Acumulados em determinada visita/Visita 5/Dados'
if os.path.exists(end):
    print('Pasta /Visita 5/Dados já existente.')
else:
    os.makedirs(end)   
    print('pasta /Visita 5/Dados criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2019_visita5.zip')
    shutil.move('PNADC_2019_visita5.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2019_visita5.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2018_visita5_20191016.zip')
    shutil.move('PNADC_2018_visita5_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2018_visita5_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2017_visita5_20191016.zip')
    shutil.move('PNADC_2017_visita5_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2017_visita5_20191016.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2016_visita5_20191016.zip')
    shutil.move('PNADC_2016_visita5_20191016.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2016_visita5_20191016.zip')
    falho = falho + 1

end = ''


#Criação da pasta Visita 5 - Documentação
end = './PNAD_2019/Acumulados em determinada visita/Visita 5/Documentação'
if os.path.exists(end):
    print('Pasta /Visita 5/Documentação já existente.')
else:
    os.makedirs(end)   
    print('pasta /Visita 5/Documentação criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/Observacoes_PNADC_2016_visita5.pdf')
    shutil.move('Observacoes_PNADC_2016_visita5.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Observacoes_PNADC_2016_visita5.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2016_visita5.txt')
    shutil.move('input_PNADC_2016_visita5.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2016_visita5.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2017_visita5.txt')
    shutil.move('input_PNADC_2017_visita5.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2017_visita5.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2018_visita5.txt')
    shutil.move('input_PNADC_2018_visita5.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2018_visita5.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2019_visita5.txt')
    shutil.move('input_PNADC_2019_visita5.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_2019_visita5.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2016_visita5.xls')
    shutil.move('dicionario_PNADC_microdados_2016_visita5.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2016_visita5.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2017_visita5.xls')
    shutil.move('dicionario_PNADC_microdados_2017_visita5.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2017_visita5.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2018_visita5.xls')
    shutil.move('dicionario_PNADC_microdados_2018_visita5.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2018_visita5.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2019_visita5.xls')
    shutil.move('dicionario_PNADC_microdados_2019_visita5.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_2019_visita5.xls')
    falho = falho + 1

end = ''



#TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL 



#Concentrados em determinado trimestre

#Criação da pasta Acumulados em determinada visita
end = './PNAD_2019/Concentrados em determinado trimestre'
if os.path.exists(end):
    print('Pasta /Concentrados em determinado trimestre já existente.')
else:
    os.makedirs(end)   
    print('pasta /Concentrados em determinado trimestre criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/LEIA-ME.pdf')
    shutil.move('LEIA-ME.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'LEIA-ME.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/PNADC_Pesquisas_Suplementares_Anuais_20200812.pdf')
    shutil.move('PNADC_Pesquisas_Suplementares_Anuais_20200812.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_Pesquisas_Suplementares_Anuais_20200812.pdf')
    falho = falho + 1

end = ''


#Geral

#Criação da pasta Geral
end = './PNAD_2019/Concentrados em determinado trimestre/Geral'
if os.path.exists(end):
    print('Pasta /Concentrados em determinado trimestre/Geral já existente.')
else:
    os.makedirs(end)   
    print('pasta /Concentrados em determinado trimestre/Geral criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/PNADcIBGE_Deflator_Anual_Trimestre.pdf')
    shutil.move('PNADcIBGE_Deflator_Anual_Trimestre.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADcIBGE_Deflator_Anual_Trimestre.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Grupamentos_ocupacionais_atividades_PNADC.pdf')
    shutil.move('Grupamentos_ocupacionais_atividades_PNADC.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Grupamentos_ocupacionais_atividades_PNADC.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Estrutura_Ocupacao_COD.xls')
    shutil.move('Estrutura_Ocupacao_COD.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'Estrutura_Ocupacao_COD.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Estrutura_Atividade_CNAE_Domiciliar_2_0.xls')
    shutil.move('Estrutura_Atividade_CNAE_Domiciliar_2_0.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'Estrutura_Atividade_CNAE_Domiciliar_2_0.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Definicao_variaveis_derivadas_PNADC_20200211.pdf')
    shutil.move('Definicao_variaveis_derivadas_PNADC_20200211.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Definicao_variaveis_derivadas_PNADC_20200211.pdf')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Chaves_PNADC.pdf')
    shutil.move('Chaves_PNADC.pdf', end)
    sucesso = sucesso + 1
except:
    print(erro+'Chaves_PNADC.pdf')
    falho = falho + 1

end = ''

#Concentrados em determinado trimestre

#Criação da pasta Trimestre 1
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 1'
if os.path.exists(end):
    print('Pasta /Trimestre 1 já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 1 criada.')

end = ''


#Trimestre 1 - Dados

#Criação da pasta Dados
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 1/Dados'
if os.path.exists(end):
    print('Pasta /Trimestre 1/Dados já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 1/Dados criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_1/Dados/informacao_importante_anual_trimestre1.txt')
    shutil.move('informacao_importante_anual_trimestre1.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'informacao_importante_anual_trimestre1.txt')
    falho = falho + 1

end = ''


#Trimestre 1 - Documentação

#Criação da pasta Documentação
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 1/Documentação'
if os.path.exists(end):
    print('Pasta /Trimestre 1/Documentação já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 1/Documentação criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_1/Documentacao/informacao_importante_anual_trimestre1.txt')
    shutil.move('informacao_importante_anual_trimestre1.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'informacao_importante_anual_trimestre1.txt')
    falho = falho + 1

end = ''


#Trimestre 2 - Dados

#Criação da pasta Dados
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 2/Dados'
if os.path.exists(end):
    print('Pasta /Trimestre 2/Dados já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 2/Dados criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2016_trimestre2_20200716.zip')
    shutil.move('PNADC_2016_trimestre2_20200716.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2016_trimestre2_20200716.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2017_trimestre2_20200716.zip')
    shutil.move('PNADC_2017_trimestre2_20200716.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2017_trimestre2_20200716.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2018_trimestre2_20200716.zip')
    shutil.move('PNADC_2018_trimestre2_20200716.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2018_trimestre2_20200716.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2019_trimestre2_20200716.zip')
    shutil.move('PNADC_2019_trimestre2_20200716.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2019_trimestre2_20200716.zip')
    falho = falho + 1

end = ''


#Trimestre 2 - Documentação

#Criação da pasta Documentação
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 2/Documentação'
if os.path.exists(end):
    print('Pasta /Trimestre 2/Documentação já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 2/Documentação criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/input_PNADC_trimestre2_20200716.txt')
    shutil.move('input_PNADC_trimestre2_20200716.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_trimestre2_20200716.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/dicionario_PNADC_microdados_trimestre2_20200716.xls')
    shutil.move('dicionario_PNADC_microdados_trimestre2_20200716.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_trimestre2_20200716.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2019_trimestre2_20200716.xls')
    shutil.move('deflator_PNADC_2019_trimestre2_20200716.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2019_trimestre2_20200716.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2018_trimestre2_20200716.xls')
    shutil.move('deflator_PNADC_2018_trimestre2_20200716.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2018_trimestre2_20200716.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2017_trimestre2_20200716.xls')
    shutil.move('deflator_PNADC_2017_trimestre2_20200716.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2017_trimestre2_20200716.xls')
    falho = falho + 1

end = ''


#Trimestre 3 - Dados

#Criação da pasta Dados
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 3/Dados'
if os.path.exists(end):
    print('Pasta /Trimestre 3/Dados já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 3/Dados criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Dados/PNADC_2019_trimestre3.zip')
    shutil.move('PNADC_2019_trimestre3.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2019_trimestre3.zip')
    falho = falho + 1

end = ''


#Trimestre 3 - Documentação

#Criação da pasta Documentação
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 3/Documentação'
if os.path.exists(end):
    print('Pasta /Trimestre 3/Documentação já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 3/Documentação criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/input_PNADC_trimestre3.txt')
    shutil.move('input_PNADC_trimestre3.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_trimestre3.txt')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/dicionario_PNADC_microdados_trimestre3.xls')
    shutil.move('dicionario_PNADC_microdados_trimestre3.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_trimestre3.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/deflator_PNADC_2019_trimestre3.xls')
    shutil.move('deflator_PNADC_2019_trimestre3.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2019_trimestre3.xls')
    falho = falho + 1

end = ''


#Trimestre 4 - Dados

#Criação da pasta Dados
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 4/Dados'
if os.path.exists(end):
    print('Pasta /Trimestre 4/Dados já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 4/Dados criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2016_trimestre4_20200429.zip')
    shutil.move('PNADC_2016_trimestre4_20200429.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2016_trimestre4_20200429.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2017_trimestre4_20200429.zip')
    shutil.move('PNADC_2017_trimestre4_20200429.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2017_trimestre4_20200429.zip')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2018_trimestre4.zip')
    shutil.move('PNADC_2018_trimestre4.zip', end)
    sucesso = sucesso + 1
except:
    print(erro+'PNADC_2018_trimestre4.zip')
    falho = falho + 1

end = ''


#Trimestre 4 - Documentação

#Criação da pasta Documentação
end = './PNAD_2019/Concentrados em determinado trimestre/Trimestre 4/Documentação'
if os.path.exists(end):
    print('Pasta /Trimestre 4/Documentação já existente.')
else:
    os.makedirs(end)   
    print('pasta /Trimestre 4/Documentação criada.')

#Trata arquivo
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/deflator_PNADC_2017_trimestre4.xls')
    shutil.move('deflator_PNADC_2017_trimestre4.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2017_trimestre4.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/deflator_PNADC_2018_trimestre4.xls')
    shutil.move('deflator_PNADC_2018_trimestre4.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'deflator_PNADC_2018_trimestre4.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/dicionario_PNADC_microdados_trimestre4_20200429.xls')
    shutil.move('dicionario_PNADC_microdados_trimestre4_20200429.xls', end)
    sucesso = sucesso + 1
except:
    print(erro+'dicionario_PNADC_microdados_trimestre4_20200429.xls')
    falho = falho + 1
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/input_PNADC_trimestre4_20200429.txt')
    shutil.move('input_PNADC_trimestre4_20200429.txt', end)
    sucesso = sucesso + 1
except:
    print(erro+'input_PNADC_trimestre4_20200429.txt')
    falho = falho + 1

end = ''

print('\nTotal: '+ falho+sucesso)
print('Sucesso: ')
print(sucesso)
print('\nFalho: ')
print(falho)

print('\nBOOOOM SHAKALAKA!!!!')
