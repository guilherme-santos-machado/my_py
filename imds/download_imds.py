import wget
import os
import shutil
from datetime import date
import zipfile

#Criação de função para download e movimentação de arquivos
def geralinkAno(link):
    for i in range(dif+1):
        anotexto = anoInicial+i 
        ano = f'{anotexto}'
        chave= ano
        lista = link+chave
        pegaETrataArquivo(lista)

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

def geralinkDia(link):
    for i in range(dif+1):
        anotexto = anoInicial+i 
        ano = f'{anotexto}'
        for i in range(12):
            i = i + 1
            if i<10:
                mes = '0'+ f'{i}'
            else:
                mes = f'{i}'
            for x in range (31):
                x=x+1
                if i<10:
                    dia = '0'+ f'{i}'
                else:
                    dia = f'{i}'
                chave= ano+mes+dia
                lista = link+chave
                pegaETrataArquivo(lista)

def linkestranho(link):
    for i in range(dif+1):
        anotexto = anoInicial+i 
        ano = f'{anotexto}'
        for i in range(12):
            i = i + 1
            if i<10:
                mes = '0'+ f'{i}'
            else:
                mes = f'{i}'
            for x in range (31):
                x=x+1
                if i<10:
                    dia = '0'+ f'{i}'
                else:
                    dia = f'{i}'
                chave= ano+mes+dia
                lista = link+chave
                pegaETrataArquivo(lista+'_SPU')
                pegaETrataArquivo(lista+'_MRE')
                pegaETrataArquivo(lista+'_MD')
                pegaETrataArquivo(lista+'_PR')

def linkMilitar(link):
    for i in range(dif+1):
        anotexto = anoInicial+i 
        ano = f'{anotexto}'
        for i in range(12):
            i = i + 1
            if i<10:
                mes = '0'+ f'{i}'
            else:
                mes = f'{i}'
            chave= ano+mes
            lista = link+chave
            pegaETrataArquivo(lista+'_Servidores')
            pegaETrataArquivo(lista+'_Militares')


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

def tirazip(source):
    files = os.listdir(source)
    for file in files:
        try: 
            extensao = file.split('.')[1]
            if extensao == 'zip':
                fantasy_zip = zipfile.ZipFile(source+file)
                fantasy_zip.extractall(source)
                fantasy_zip.close()
                os.remove(source+file)
            else:
                print(extensao,'não é um zip.')
        except:
            print(file+' é uma pasta.')


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



#Cartão de Pagamento
geralink('http://www.portaltransparencia.gov.br/download-de-dados/cpgf/')
geralink('http://www.portaltransparencia.gov.br/download-de-dados/cpcc/')
geralink('http://www.portaltransparencia.gov.br/download-de-dados/cpdc/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./cartao')

#CNPJ
geralink('http://www.portaltransparencia.gov.br/download-de-dados/favorecidos-pj/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./cnpj')

#Convenios
geralinkDia('http://www.portaltransparencia.gov.br/download-de-dados/convenios/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./convenios')

#Despesas públicas
geralinkDia('http://www.portaltransparencia.gov.br/download-de-dados/despesas/')
geralink('http://www.portaltransparencia.gov.br/download-de-dados/despesas-execucao/')
geralink('http://www.portaltransparencia.gov.br/download-de-dados/transferencias/')
geralink('http://www.portaltransparencia.gov.br/download-de-dados/despesas-favorecidos/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./despesas publicas')

#Emendas
wget.download('http://www.portaltransparencia.gov.br/download-de-dados/emendas-parlamentares/UNICO')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./emendas')

#Imóveis
linkestranho('http://www.portaltransparencia.gov.br/download-de-dados/imoveis-funcionais/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./imoveis')

#Licitações
geralink('http://www.portaltransparencia.gov.br/download-de-dados/licitacoes/')
geralink('http://www.portaltransparencia.gov.br/download-de-dados/compras/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./licitacoes')

#Orçamento
geralinkAno('http://www.portaltransparencia.gov.br/download-de-dados/orcamento-despesa/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./orcamento')

#Receitas
geralinkAno('http://www.portaltransparencia.gov.br/download-de-dados/receitas/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./receitas')

#Sanções
geralinkDia('http://www.portaltransparencia.gov.br/download-de-dados/ceis/')
geralinkDia('http://www.portaltransparencia.gov.br/download-de-dados/cepim/')
geralinkDia('http://www.portaltransparencia.gov.br/download-de-dados/cnep/')
geralinkDia('http://www.portaltransparencia.gov.br/download-de-dados/acordos-leniencia/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./sancoes')

#Servidores
geralink('http://www.portaltransparencia.gov.br/download-de-dados/pep/')
geralinkDia('http://www.portaltransparencia.gov.br/download-de-dados/ceaf/20201019')
linkMilitar('http://www.portaltransparencia.gov.br/download-de-dados/servidores/')
movimentaArquivo(source='./', destination='./download')
tirazip(source='./download')
movimentaArquivo(source='./download', destination='./servidores')

#Viagens