import wget
import os
import shutil

#Criação de função para download e tratamento de arquivos
def pegaETrataArquivo (lista):  
    for item in lista:
        try:
            wget.download(item)      

        except:
            print('\nDownload falhou '+ item)

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


pegaETrataArquivo(lista=[])
movimentaArquivo(source='', destination='')
