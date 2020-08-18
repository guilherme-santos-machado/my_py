import wget
import os
import shutil

sucesso = 0
falho = 0
def download (url, file, end):    
    try:
        wget.download(url)  
        shutil.move(file, end)      
        sucesso =+ 1
        return sucesso
    except:
        print('Download falhou '+ file)
        falho =+ 1
        return falho



    
download('ftp://ftp.ibge.gov.br/Trabalho_e_Rendimento/Pesquisa_Nacional_por_Amostra_de_Domicilios_continua/Anual/Microdados/LEIA-ME.pdf','LEIA-ME.PDF', './Em teste')









