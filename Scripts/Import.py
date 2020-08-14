import urllib.request
import time
import os
import shutil
from datetime import date

#Valor do end_Time e sleepTime devem ser apresentados em segundos
end_time = time.time() + 900
countTimer = 900
sleepTime = 0
#####################################################################################
anoCriacao = 2018
contador = 0
#####################################################################################
print ('Criando pasta no endereço solicitado')
os.chdir('\macha\Documents\FAESA\devWeb1')
os.mkdir ('/temp')
print ('Pasta criada.')
while contador == 0 :
    print('Iniciando busca de arquivo...')
    dataAtual = date.today()
    yearSistema = dataAtual.year
    if (anoCriacao > yearSistema):
        print('Download Error') 
        print('Script não faz download de anos anteriores do ano de criação:', anoCriacao)
    else:
        if (anoCriacao == yearSistema):       
            print('File Download Start from year:', anoCriacao)
            url = 'http://www.mdic.gov.br/balanca/bd/comexstat-bd/ncm/EXP_'+str(anoCriacao)+'.csv'
            urllib.request.urlretrieve(url, 'Exportação_'+str(anoCriacao)+'.csv')
            contador +=1
            print ('File Download Over... Version:', contador)
        else:
            print('File Download Start from year:', yearSistema)
            url = 'http://www.mdic.gov.br/balanca/bd/comexstat-bd/ncm/EXP_'+str(yearSistema)+'.csv'
            urllib.request.urlretrieve(url, 'Exportação_'+str(yearSistema)+'.csv')
            contador +=1
            print ('File Download Over... Version:', contador)    

    countTimer += sleepTime
    contador = contador + 1

shutil.move('Exportação_'+str(anoCriacao)+'.csv', "/tmp")
print('System down')