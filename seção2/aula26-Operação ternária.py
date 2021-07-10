
# logged_user = False
# msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar.'
# print(msg)


idade = input('Qual e sua idade: ')

if not idade.isnumeric():
    print('Voce precisa digitar um numero.')
else:
    idade = int(idade)
    e_de_maior = idade >= 18
    msg = 'Pode acessar' if e_de_maior else 'Nao pode acessar'
    print(msg)

