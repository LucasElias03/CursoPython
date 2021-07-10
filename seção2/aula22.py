'''
variavel = ['Lucas', 'Maria', 'João']


comeca_com_l = False
for valor in variavel:
    if valor.lower().startswith('l'):
       comeca_com_l = True

if comeca_com_l:
    print('Existe uma paralvra que começa com L.')
else:
    print('Não existe palavra com a letra L.')
'''


variavel = ['aLucas', 'Maria', 'João']



for valor in variavel:
    print(valor)
    if valor.lower().startswith('l'):
      break

else:
    print('Não existe palavra com a letra L.')




