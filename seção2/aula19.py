
# nome = 'Lucas Elias Camilo'
#
# for n, letra in enumerate(nome):
#     print(n, letra)


nome = 'lucas'
nova_string = ''

for letra in nome:
    if letra == 'l':
        nova_string = nova_string + letra.upper()
    else:
        nova_string = nova_string + letra
print(nova_string)
