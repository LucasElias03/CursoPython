
nome = 'Lucas Elias Camilo'
tamanho_nome = len(nome)
contador = 0
nova_string = ''

while contador < tamanho_nome:
    letra = nome[contador]
    if letra == 'a':
       nova_string = nova_string + 'A'
    else:
        nova_string = nova_string + letra

    contador = contador + 1

print(nova_string)







