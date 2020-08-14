import os
import shutil


if os.path.exists("./t1_py"):
    print('Pasta já existente.')
else:
    os.makedirs('./t1_py')
    #shutil.move("teste.txt", "./t1_py")
    #os.makedirs('./t2_py')
    print('pasta criada.')



