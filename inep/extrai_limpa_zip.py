import zipfile
import os
         
source = "./download/"

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
