'''
count - Itertools / E um iterador
'''
from itertools import count

contador = count(start=1, step=2, )

# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
#
# for valor in contador:
#     print(valor)
#
#     if valor >= 10:
#         break


lista = ['Lucas', 'João', 'Maria', 'Pedro', 'Elias' ]

lista = zip(contador, lista)
print(list(lista))
