
def func(funcao, *args):
    return funcao(*args)


def name(nome):
    return f'{nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = func(name, 'Lucas')
print(executando)






# def ola_mundo():
#     return 'Olá Mundo'
#
# def mestre(variavel):
#     return variavel
#
# executando = mestre(ola_mundo())
# print(executando)



# def mestre(funcao, *args, **kwargs):
#     return funcao(*args,**kwargs)
#
#
# def fala_oi(nome):
#     return f'Oi {nome}'
#
#
# def saudacao(nome, saudacao):
#     return f'{saudacao} {nome}'
#
# executando = mestre(fala_oi, 'Lucas')
# print(executando)
#
# executando2 = mestre(saudacao, 'Lucas', saudacao = 'Bom Dia')
# print(executando2)


