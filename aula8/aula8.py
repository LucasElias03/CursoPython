nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80
imc = peso/(altura**2)
ano_atual = 2021
ano_nasc = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura:.2f} de altura e peso {peso}Kg.')
print(f'{nome} pesa {peso} e seu imc é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nasc}.')