class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as erro:
    print(f'Erro: {erro}')


