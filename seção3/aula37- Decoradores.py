
# def fala_oi():
#     print('Oi')
#
# variavel = fala_oi
# variavel()



# def master():
#     def slave():
#         print('Oi')
#     return slave
#
# variavel = master()
# variavel()
# print(type(variavel))





# '''
# Função decoradora
# '''
# def master(funcao):
#     def slave(*args, **kwargs):
#         print('Agora estou decorada.')
#         funcao(*args, **kwargs)
#     return slave
#
# '''
# Decorador - @
# '''
# @master  # ele serve pra jogar a função fala_oi() dentro do parâmetro funcao que está na função master. exato (é um decorador)
# def fala_oi():
#     print('Oi')
#
# @master
# def outra_funcao(msg):
#     print(msg)
#
# outra_funcao('Olá, eu sou Lucas.')








# from time import time
# from time import sleep
#
#
# def velocidade(funcao):
#     def interna(*args, **kwargs):
#         start_time = time()
#         resultado = funcao(*args, **kwargs)
#         end_time = time()
#         tempo = (start_time - end_time) * 1000
#         print(f'A função {funcao.__name__} levou {tempo:.2f}ms para executar.')
#         return resultado
#     return interna
#
#
# @velocidade
# def demora():
#     for i in range(5):
#         print(i)
#         sleep(1)
#
# demora()
