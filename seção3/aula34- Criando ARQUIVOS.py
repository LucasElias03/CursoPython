
# file = open('abc.txt', 'w+')
# file.write('Linha 1\n')
# file.write('Linha 2\n')
# file.write('Linha 3\n')
# # file.seek(0, 0) - Puxando o cursor para o  inicio do arquivo
# file.seek(0, 0)
# print('Lendo linhas:')
# print(file.read())
# print('-----------------------')
#
# file.seek(0, 0)
# # Lendo linha por linha do arquivo
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='' )
# print('-----------------------')
#
# file.seek(0, 0)
# # Jogar linha por linha em uma lista
# # print(file.readlines())
# for linha in file.readlines():
#     print(linha, end='' )
#
# file.close()






# try:
#     file = open('abc.txt', 'w+')
#     file.write('Linha')
#
#     file.seek(0,0)
#     print(file.read())
# finally:
#     file.close()








'''
Melhor forma de trabalhar com arquivo
'''
# (with)- Gerenciador de contexto vai abrir o arquivo e fechar ao acabar a execução.

#          (ARQUIVO) (MODO)   (VARIÁVEl)
with open('abc.txt', 'w+') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0,0)
    print(file.read())




'''
Apagando arquivo
'''

# import os
# os.remove('abc.txt')

