import os
import shutil

caminho_original = '/home/lucas/Música'
caminho_novo = '/home/lucas/Música2'

try: #Criando (caminho novo)
    os.mkdir(caminho_novo)
except FileExistsError:
    print(f'Pasta {caminho_novo} já existe.')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        #Movendo arquivo old para new
        shutil.move(old_file_path, new_file_path)

        #Copiando arquivo old para new
        shutil.copy(old_file_path, new_file_path)

        #Apagar Arquivo
        os.remove(new_file_path)