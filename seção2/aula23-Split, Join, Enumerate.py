'''
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumera elementos da lista # iterável
'''

# string = 'O Brasil é o país do futbol, o Brasil é penta.'
# lista_1 = string.split(' ')
# lista_2 = string.split(',')
#
# palavra = ''
# contagem = 0
# for valor in lista_1:
#     qtd_vezez = lista_1.count(valor)
#
#     if qtd_vezez > contagem:
#         contagem = qtd_vezez
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')


# string = 'O Brasil é penta.'
# lista = string.split(' ')
# string_2 = ' '.join(lista)
#
# print(string)
# print(lista)
# print(string_2)


string = ['Lucas','João','Maria']


for indice, valor in enumerate(string):
    print(indice,valor )




