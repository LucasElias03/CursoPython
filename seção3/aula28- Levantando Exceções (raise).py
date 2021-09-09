#
# def divide(n1, n2):
#     try:
#         return n1 / n2
#     except ZeroDivisionError as erro:
#         print('Não e permitido dividir por zero')
#         raise
#
# print(divide(2,0))




def dividir(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0 ')
    return n1 / n2


try:
    print(dividir(2,0))
except ValueError as erro:
    print(erro)

