produtos = [
    {'nome': 'p1', 'preco': 13},
    {'nome': 'p1', 'preco': 55.55},
    {'nome': 'p1', 'preco': 2.58},
    {'nome': 'p1', 'preco': 22},
    {'nome': 'p1', 'preco': 81.25},
    {'nome': 'p1', 'preco': 40},
    {'nome': 'p1', 'preco': 7.98}
]

pessoas = [
    {'nome': 'Luiz', 'idade': 13},
    {'nome': 'Eduardo', 'idade': 44},
    {'nome': 'Lucas', 'idade': 16},
    {'nome': 'Maria', 'idade': 22},
    {'nome': 'João', 'idade': 36},
    {'nome': 'Carlos', 'idade': 43},
    {'nome': 'Amanda', 'idade': 18}
]

lista = [1,2,3,4,5,6,7]

from functools import reduce

# acumula = 0
# for item in lista:
#     acumula = acumula + item
# print(acumula)

'''
Ex. Lista
'''
# soma_lista = reduce(lambda ac, i: i + ac, lista, 0)
# print(soma_lista)



'''
Ex. Produtos
'''
# soma_preco = reduce(lambda ac, p:p['preco'] + ac, produtos,0 )
# print(soma_preco)



'''
Ex. Pessoas
'''
#                                                          Valor Inicial
soma_idade = reduce(lambda ac, p:p['idade'] + ac, pessoas, 0)
print(soma_idade / len(pessoas))


