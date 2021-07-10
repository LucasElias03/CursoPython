
nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))
idade_menor = 20
idade_maior = 30



if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode receber o imprestimo ')
else:
    print(f'{nome} NãO pode receber o imprestimo')
