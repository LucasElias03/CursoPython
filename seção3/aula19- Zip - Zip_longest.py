'''
Zip - Unindo iteravéis
Zip_longest - Itertools
'''
#                                (contador)
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo','João Pessoa', 'Natal', 'Recife']
estados = ['SP', 'PB', 'RN']

estados_cidades = zip(indice, estados, cidades,)

for indice, estados, cidades in estados_cidades:
    print(indice, estados, cidades)

