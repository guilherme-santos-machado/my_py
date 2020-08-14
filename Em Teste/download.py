import wget
erro = 'Arquivo não disponível, favor verificar a FPT fo arquivo '





#ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL ANUAL





#Informações sobre os arquivos de Microdados, Pesquisas Suplementares Anuais e Histórico completo de atualizações
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/LEIA-ME.pdf')
except:
    print(erro+'LEIA-ME.pdf.')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf')
except:
    print(erro+'PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf.')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/atualizacoes_divulgacao_anual_20200716.txt')
except:
    print(erro+'atualizacoes_divulgacao_anual_20200716.txt')
      

# Acumulados em determinada visita
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/LEIA-ME.pdf')
except:
    print(erro+'LEIA-ME.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf')
except:
    print(erro+'PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf')
#Geral - Acumulados em determinada visita
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Chaves_PNADC.pdf')
except:
    print(erro+'Chaves_PNADC.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Definicao_variaveis_derivadas_PNADC_20200211.pdf')
except:
    print(erro+'Definicao_variaveis_derivadas_PNADC_20200211.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflacionamento_PNADC_anual_visita.txt')
except:
    print(erro+'deflacionamento_PNADC_anual_visita.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2017.xls')
except:
    print(erro+'deflator_PNADC_2017.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2018.xls')
except:
    print(erro+'deflator_PNADC_2018.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/deflator_PNADC_2019.xls')
except:
    print(erro+'deflator_PNADC_2019.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Estrutura_Atividade_CNAE_Domiciliar_2_0.xls')
except:
    print(erro+'Estrutura_Atividade_CNAE_Domiciliar_2_0.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Estrutura_Ocupacao_COD.xls')
except:
    print(erro+'Estrutura_Ocupacao_COD.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/Grupamentos_ocupacionais_atividades_PNADC.pdf')
except:
    print(erro+'Grupamentos_ocupacionais_atividades_PNADC.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/historico_temas_PNADC_anual_visita_20200506.txt')
except:
    print(erro+'historico_temas_PNADC_anual_visita_20200506.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Documentacao_Geral/PNADcIBGE_Deflator_Anual_Visita.pdf')
except:
    print(erro+'PNADcIBGE_Deflator_Anual_Visita.pdf')
#Acumulados em determinada visita
#Visita 1 - Dados
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2012_visita1_20191016.zip')
except:
    print(erro+'PNADC_2012_visita1_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2013_visita1_20191016.zip')
except:
    print(erro+'PNADC_2013_visita1_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2014_visita1_20191016.zip')
except:
    print(erro+'PNADC_2014_visita1_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2015_visita1_20191016.zip')
except:
    print(erro+'PNADC_2015_visita1_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2016_visita1_20191016.zip')
except:
    print(erro+'PNADC_2016_visita1_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2017_visita1_20191016.zip')
except:
    print(erro+'PNADC_2017_visita1_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2018_visita1_20191218.zip')
except:
    print(erro+'PNADC_2018_visita1_20191218.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Dados/PNADC_2019_visita1.zip')
except:
    print(erro+'PNADC_2019_visita1.zip')
#Visita 1 - Documentação
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2012_a_2014_visita1.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2012_a_2014_visita1.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2015_visita1.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2015_visita1.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2016_visita1.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2016_visita1.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2017_visita1.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2017_visita1.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2018_visita1.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2018_visita1.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/dicionario_PNADC_microdados_2019_visita1.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2019_visita1.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2012_a_2014_visita1.txt')
except:
    print(erro+'input_PNADC_2012_a_2014_visita1.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2015_visita1.txt')
except:
    print(erro+'input_PNADC_2015_visita1.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2016_visita1.txt')
except:
    print(erro+'input_PNADC_2016_visita1.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2017_visita1.txt')
except:
    print(erro+'input_PNADC_2017_visita1.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2018_visita1.txt')
except:
    print(erro+'input_PNADC_2018_visita1.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/input_PNADC_2019_visita1.txt')
except:
    print(erro+'input_PNADC_2019_visita1.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_1/Documentacao/Observacoes_PNADC_2015_2016_visita1.pdf')
except:
    print(erro+'Observacoes_PNADC_2015_2016_visita1.pdf')
#Visita 2 - Dados
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2016_visita5_20191016.zip')
except:
    print(erro+'PNADC_2016_visita5_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2017_visita5_20191016.zip')
except:
    print(erro+'PNADC_2017_visita5_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2018_visita5_20191016.zip')
except:
    print(erro+'PNADC_2018_visita5_20191016.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Dados/PNADC_2019_visita5_20191016.zip')
except:
    print(erro+'PNADC_2019_visita5_20191016.zip')
#Visita 2 - Documentação
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/Observacoes_PNADC_2016_visita5.pdf')
except:
    print(erro+'Observacoes_PNADC_2016_visita5.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2016_visita5.txt')
except:
    print(erro+'input_PNADC_2016_visita5.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2017_visita5.txt')
except:
    print(erro+'input_PNADC_2017_visita5.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2018_visita5.txt')
except:
    print(erro+'input_PNADC_2018_visita5.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/input_PNADC_2019_visita5.txt')
except:
    print(erro+'input_PNADC_2019_visita5.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2016_visita5.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2016_visita5.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2017_visita5.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2017_visita5.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2018_visita5.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2018_visita5.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Visita/Visita_5/Documentacao/dicionario_PNADC_microdados_2019_visita5.xls')
except:
    print(erro+'dicionario_PNADC_microdados_2019_visita5.xls')






#TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL TRIMESTRAL 





#Concentrados em determinado trimestre
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/LEIA-ME.pdf')
except:
    print(erro+'LEIA-ME.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/PNADC_Pesquisas_Suplementares_Anuais_20200812.pdf')
except:
    print(erro+'PNADC_Pesquisas_Suplementares_Anuais_20200812.pdf')
#Geral - Concentrados em determinado trimestre
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/PNADcIBGE_Deflator_Anual_Trimestre.pdf')
except:
    print(erro+'PNADcIBGE_Deflator_Anual_Trimestre.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Grupamentos_ocupacionais_atividades_PNADC.pdf')
except:
    print(erro+'Grupamentos_ocupacionais_atividades_PNADC.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Estrutura_Ocupacao_COD.xls')
except:
    print(erro+'Estrutura_Ocupacao_COD.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Estrutura_Atividade_CNAE_Domiciliar_2_0.xls')
except:
    print(erro+'Estrutura_Atividade_CNAE_Domiciliar_2_0.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Definicao_variaveis_derivadas_PNADC_20200211.pdf')
except:
    print(erro+'Definicao_variaveis_derivadas_PNADC_20200211.pdf')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Documentacao_Geral/Chaves_PNADC.pdf')
except:
    print(erro+'Chaves_PNADC.pdf')

#Concentrados em determinado trimestre
#Trimestre 1 - Dados
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_1/Dados/informacao_importante_anual_trimestre1.txt')
except:
    print(erro+'informacao_importante_anual_trimestre1.txt')
#Trimestre 1 - Documentação
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_1/Documentacao/informacao_importante_anual_trimestre1.txt')
except:
    print(erro+'informacao_importante_anual_trimestre1.txt')
#Trimestre 2 - Dados
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2016_trimestre2_20200716.zip')
except:
    print(erro+'PNADC_2016_trimestre2_20200716.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2017_trimestre2_20200716.zip')
except:
    print(erro+'PNADC_2017_trimestre2_20200716.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2018_trimestre2_20200716.zip')
except:
    print(erro+'PNADC_2018_trimestre2_20200716.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Dados/PNADC_2019_trimestre2_20200716.zip')
except:
    print(erro+'PNADC_2019_trimestre2_20200716.zip')
#Trimestre 2 - Documentação
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/input_PNADC_trimestre2_20200716.txt')
except:
    print(erro+'input_PNADC_trimestre2_20200716.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/dicionario_PNADC_microdados_trimestre2_20200716.xls')
except:
    print(erro+'dicionario_PNADC_microdados_trimestre2_20200716.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2019_trimestre2_20200716.xls')
except:
    print(erro+'deflator_PNADC_2019_trimestre2_20200716.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2018_trimestre2_20200716.xls')
except:
    print(erro+'deflator_PNADC_2018_trimestre2_20200716.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_2/Documentacao/deflator_PNADC_2017_trimestre2_20200716.xls')
except:
    print(erro+'deflator_PNADC_2017_trimestre2_20200716.xls')
#Trimestre 3 - Dados
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Dados/PNADC_2019_trimestre3.zip')
except:
    print(erro+'PNADC_2019_trimestre3.zip')
#Trimestre 3 - Documentação
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/input_PNADC_trimestre3.txt')
except:
    print(erro+'input_PNADC_trimestre3.txt')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/dicionario_PNADC_microdados_trimestre3.xls')
except:
    print(erro+'dicionario_PNADC_microdados_trimestre3.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_3/Documentacao/deflator_PNADC_2019_trimestre3.xls')
except:
    print(erro+'deflator_PNADC_2019_trimestre3.xls')
#Trimestre 4 - Dados
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2016_trimestre4_20200429.zip')
except:
    print(erro+'PNADC_2016_trimestre4_20200429.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2017_trimestre4_20200429.zip')
except:
    print(erro+'PNADC_2017_trimestre4_20200429.zip')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Dados/PNADC_2018_trimestre4.zip')
except:
    print(erro+'PNADC_2018_trimestre4_20200429.zip')
#Trimestre 4 - Documentação
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/deflator_PNADC_2017_trimestre4.xls')
except:
    print(erro+'deflator_PNADC_2017_trimestre4.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/deflator_PNADC_2018_trimestre4.xls')
except:
    print(erro+'deflator_PNADC_2018_trimestre4.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/dicionario_PNADC_microdados_trimestre4_20200429.xls')
except:
    print(erro+'dicionario_PNADC_microdados_trimestre4_20200429.xls')
try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/Trimestre/Trimestre_4/Documentacao/input_PNADC_trimestre4_20200429.txt')
except:
    print(erro+'input_PNADC_trimestre4_20200429.txt')
