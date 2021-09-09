
try:
    a = {}
    print(a)
except NameError as erro:
    print('Erro do desenvolvedor')
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave')
except Exception as erro:
    print('Ocorreu um erro inesperado:',)
# "else" vai se executado sempre que o codigo for executador sem nenhum erro.
else:
    print('Seu código foi execultado com sucesso!')
# "finally" vai ser execultada sempre
finally:
    print('Finalmente')
