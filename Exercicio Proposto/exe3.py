
nome = input('Digite seu primeiro nome: ')
quant_letra = len(nome)

if quant_letra < 4:
    print('Seu nome é curto.')
elif quant_letra >= 5 and quant_letra <= 6:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')
