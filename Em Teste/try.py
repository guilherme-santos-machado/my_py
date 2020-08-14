import wget

try:
    wget.download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/PNADC_Pesquisas_Suplementares_Anuais_20200715.pdf')
except :
    print('arquivo não disponível.')

print('Fim do Script')