import wget
import os
import shutil
from datetime import date
k = date.today()


anoInicial = 2012
thisYear = k.year
pdf = '.pdf'
txt = '.txt'


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


criaContinuacao('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/PNADC_Pesquisas_Suplementares_Anuais_', pdf)
