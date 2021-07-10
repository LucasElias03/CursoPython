#
# def funcao(arg,arg2):
#     return arg * arg2
#
# var = funcao(2,2)
# print(var)


'''
Expressão lambda (Função anônima)
'''

# a = lambda arg, arg2: arg * arg2
#
# print(a(2,2))


# - Exemplo

# lista = [
#     ['P1', 13],
#     ['P2', 6],
#     ['P3', 7],
#     ['P4', 50],
#     ['P5', 8],
# ]
#
# # def funcao(item):
# #     return item[1]
# #
# # lista.sort(key=funcao )
# # print(lista)
#
# lista.sort(key=lambda item: item[1])
# print(lista)






# Programa para filtrar apenas os itens pares de uma lista
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)



