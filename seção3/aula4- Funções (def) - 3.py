'''
Desempacotamento
'''
lista = [1,2,3,4,5,6,7,8,9]

print(*lista, sep=' ')


'''
Funções (def) em Python - *args **kwargs 
'''
# def funcao(*args):
#     print(args)
#     print(args[0])
#     print(args[-1])
#     print(len(args))
#
# funcao(1,2,3,4,5)


'''
Tranformando uma Tupla em uma lista.
'''
# def funcao(*args):
#     args = list(args)
#     args[0] = 20
#     print(args)
#
# funcao(1,2,3,4,5)


'''
Lista desenpacotada dentro de uma Tupla
'''
# def funcao(*args):
#      print(args[1])
#
# lista = [1,2,3,4,5]
# funcao(*lista, 56,57)




# def funcao(*args,**kwargs):
#     print(args)
#     print(kwargs['nome'], kwargs['sobrenome'])
#     idade = kwargs.get('idade')
#     print(idade)
#
# lista = [1, 2, 3, 4, 5]
# funcao(*lista, 56, 57, nome = 'Lucas', sobrenome = 'Elias', idade = 18)
