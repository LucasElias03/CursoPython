
# d1 = {'chave1':'Valor da chave'}
# d1['nova_chave'] = 'Valor da nova chave'
#
# print(d1['chave1'])


'''
Outro jeito de criar um dicionário
'''

# d1 = dict(chave1='Valor da chave', chave2='VAlor da outra chave')
# print(d1)
# print(d1['chave1'])
# print(d1['chave2'])




# d1 = {
#     'stg': 'Valor',
#       123: 'Outro valor',
#     (1,2,3): 'Tupla',
# }
#
# d1['naoexiste'] = 'Agora existe'
#
# if 'naoexiste' in d1:
#     print(d1['naoexiste'])
#
# print('OI')
#




# d1 = {
#     'stg': 'Valor',
#       123: 'Outro valor',
#     (1,2,3): 'Tupla',
# }
#
# d1['novachave'] = 'Agora ela existe'
#
# if d1.get('novachave') is not None:
#     print(d1.get('novachave'))
#
# print(123)






# d1 = {
#     'str': 'Valor',
#       123: 'Outro valor',
#     (1,2,3): 'Tupla',
# }
#
# print('str' in d1)
# #                chaves
# print('str' in d1.keys())
# #                   valor
# print('Valor' in d1.values())




'''
Iterar sobre um dicionário
'''
d1 = {
    'chave1' : 'Valor',
    'chave2' : 'Outro valor',
    'chave3' : 'Tupla',
}

for v in d1.values():
    print(v)

for k, v in d1.items():
    print(k , v)



