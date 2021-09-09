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

'''
COM LISTA
'''
nova_lista = filter(lambda x:x > 4, lista)
print(list(nova_lista))


'''
COM PRODUTOS
'''
# nova_lista1 = filter(lambda p:p['preco'] > 20, produtos)
# for preco in nova_lista:
#     print(preco)

'''
COM PESSOAS
'''
# def filte(i):
#     if i['idade'] >= 18:
#         return True


# nova_lista2 = filter(filte,pessoas)

# nova_lista2 = filter(lambda i:i['idade'] >= 18, pessoas)
# for idade in nova_lista2:
#     print(idade)
