
# lista = [
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
#     ('chave3', 'valor3')
# ]
#
# d1 = {x: y*2 for x,y in lista}
# print(d1)






d1 = {x: y for x,y in enumerate(range(5))}
print(d1)

d2 = {f'chave{x}': x*2 for x in range(5)}
print(d2)




