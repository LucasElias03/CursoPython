'''
 1° - Exercicio
'''

# def funcao(saudacao, nome ):
#     print(saudacao, nome)
#
# funcao('Olá', 'Lucas')

'''
 2° - Exercicio
'''

# def soma(n1,n2,n3):
#     print(n1 + n2 + n3)
#
# soma(2,4,2)

'''
 3° - Exercicio
'''

# def funcao(n1,n2):
#     return n1 +(n1 * (n2/100))
#
# resultado = funcao(15,100)
# print(resultado)


'''
 4° - Exercicio
'''

# def funcao(n1):
#     return n1
#
# numero = funcao(15)
#
# if numero % 3 == 0 and numero % 5 == 0:
#     print('FizzBuzz')
# elif numero % 3 == 0:
#     print('Fizz')
# elif  numero % 5 == 0:
#     print('Buzz')
# else:
#     print(numero)

'''
'''

def fb(n1):
    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'FizzBuzz'
    if n1 % 5 == 0:
        return 'Fizz'
    if n1 % 3 == 0:
        return 'Buzz'
    return n1

print(fb(150))


