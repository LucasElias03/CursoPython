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



nova_lista = map(lambda x:x*2, lista)
print(list(nova_lista))

