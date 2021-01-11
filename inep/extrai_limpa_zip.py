#Importação de bibliotecas
import zipfile
import os
         
#Pega o endereço da pasta         
source = "./download/"

#Cria uma Lista com o nome dos arquivos
files = os.listdir(source)
for file in files:
    try: 
        #Separa os arquivos pela extensão
        extensao = file.split('.')[1]
        if extensao == 'zip':
            #tira todos os arquivos do zip e exclui o arquivo zipado
            fantasy_zip = zipfile.ZipFile(source+file)
            fantasy_zip.extractall(source)
            fantasy_zip.close()
            os.remove(source+file)
        else:
            print(extensao,'não é um zip.')
    except:
        print(file+' é uma pasta.')
