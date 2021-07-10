
# clientes = {
#     'cliente1': {
#         'nome': 'Lucas',
#         'sobrenome': 'Elias',
#     },
#     'cliente2': {
#         'nome': 'João',
#         'sobrenome': 'Moreira',
#     },
# }
#
#
# for cliente_chave, cliente_valor in clientes.items():
#     print(f'Exibindo {cliente_chave}')
#     for dados_chaves, dados_valor in cliente_valor.items():
#         print(f'\t{dados_chaves} = {dados_valor}')






# d1 = {
#     1: 2,
#     2: 3,
#     4: 5
# }
# # # Elimina uma chave
# # d1.pop(4)
# # print(d1)
#
# # Elimina a ultima chave
# d1.popitem()
# print(d1)





'''
Concatenar dois dicionário
'''
d1 = {
    1: 2,
    2: 3,
    4: 5
}

d2 = {
    'a': 'b',
    'c': 'd'
}

d1.update(d2)
print(d1)