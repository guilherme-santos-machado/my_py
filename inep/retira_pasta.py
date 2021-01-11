#Importação de bibliotecas
import os
import shutil

#Aponta a fonte e destino
source = "./download/"
destination = "./download"

#Pega os arquivos e cria uma LISTA
files = os.listdir(source)
for file in files:

    try: 
        extensao = file.split('.')[1]
        # if extensao != 'git':
        #     shutil.move(f"{source}/{file}", destination)
        # else:
        #     print('TA TENTANDO MOVER MEU .GIT?')
    except:
        nova_pasta=source+file+'/'
        novo_files = os.listdir(nova_pasta)
        for subArquivos in novo_files:
            try:
                #Move arquivo da pasta retirada do zip, para a pasta de download
                extensao = subArquivos.split('.')[1]
                if extensao == 'xls' or 'xlsx' or 'ods' or 'db':
                    shutil.move(f"{nova_pasta}/{subArquivos}", destination)
                else:
                    os.remove(nova_pasta+subArquivos)
            except:
                print('nada')


#Apaga todas as pastas dentro de ./download
files = os.listdir(source)
for file in files:
    try: 
        extensao = file.split('.')[1]
        if extensao != 'git':
            print('----')
        else:
            print('pasta é um .GIT?')
    except:
        print(file+' é uma pasta.')
        shutil.rmtree(source+file, ignore_errors=True)
        print(file+' foi apagado.')