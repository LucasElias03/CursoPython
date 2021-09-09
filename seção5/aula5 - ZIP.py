from zipfile import ZipFile
import os

'''
Criando arquivo zip é adiciona aquivos 
'''

caminho = '/home/lucas/Música'
with ZipFile('arquivo.zip', 'w') as zip:
    for arquivo in os.listdir(caminho):
        caminho_completo = os.path.join(caminho, arquivo)
        zip.write(caminho_completo, arquivo)


'''
Lendo arquivo zip
'''
with ZipFile('arquivo.zip', 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)


'''
Extraindo arquivo zip em pasta 'descompactada'
'''
with ZipFile('arquivo.zip', 'r') as zip:
    zip.extractall('descompactado')



