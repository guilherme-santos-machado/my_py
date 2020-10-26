import wget
import os
import shutil
from datetime import date

#Criação de função para download e movimentação de arquivos
def geralink(link):
    for i in range(dif+1):
        anotexto = anoInicial+i 
        ano = f'{anotexto}'
        for i in range(12):
            i = i + 1
            if i<10:
                dia = '0'+ f'{i}'
            else:
                dia = f'{i}'
            chave= ano+dia
            lista = link+chave
            pegaETrataArquivo(lista)
def pegaETrataArquivo (lista):  
        try:
            wget.download(lista)      

        except:
            print('\nDownload falhou '+ lista)

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


k = date.today()
anoInicial = 2013
thisYear = k.year
dif = thisYear- anoInicial

destination = './download'
if os.path.exists(destination):
    print('\nPasta /Download já existente.')
else:
    os.makedirs(destination)   
    print('\npasta /Download criada.')


#Cartão de Pagamento do Governo Federal (CPGF)
geralink('http://www.portaltransparencia.gov.br/download-de-dados/cpgf/')
geralink('http://www.portaltransparencia.gov.br/download-de-dados/cpcc/')
geralink('http://www.portaltransparencia.gov.br/download-de-dados/cpdc/')
movimentaArquivo(source='./', destination='./download')