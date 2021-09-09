"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0 4 2 5 2 0 1 1 0 0 0 1
5 4 3 2 9 8 7 6 5 4 3 2
0 16 6 10 18 0 7 6 0 0 0 2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0 4 2 5 2 0 1 1 0 0 0 1 1 X
6 5 4 3 2 9 8 7 6 5 4 3 2
0 20 8 15 4 0 8 7 0 0 0 3 2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado 茅 maior que 9, ent茫o 茅 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original = 04.252.011/0001-10
Valido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

while True:
    cnpj = '24.252.011/0001-10'
    cnpj_original = cnpj

    soma_cnpj = '543298765432'
    soma_cnpj2 = '6543298765432'


    def remover_caractere(cnpj):
        cnpj = cnpj.replace('.','')
        cnpj = cnpj.replace('/','')
        cnpj = cnpj.replace('-','')
        return cnpj

    def eh_sequencia(cnpj):
        sequencia = cnpj[0] * len(cnpj)
        if sequencia == cnpj:
            return True
        else:
            return False


    def soma_lista(lista):
        soma = 0
        for x in lista:
            soma = soma + x
        return soma

    def lista_multi(cnpj, soma_cnpj):
        lista_multip = []
        for a, b in zip(cnpj, soma_cnpj):
            lista_multip.append(int(a) * int(b))
        return lista_multip


    cnpj = remover_caractere(cnpj)
    if eh_sequencia(cnpj):
        print('É uma sequencia')
        break

    cnpj = list(cnpj[0:12])

    lista_multiplicada = lista_multi(cnpj,soma_cnpj)

    total_soma_lista = soma_lista(lista_multiplicada)

    primeiro_digito = 11 - (total_soma_lista % 11)
    if primeiro_digito > 9:
        primeiro_digito = 0
    else:
        pass
    cnpj.append(str(primeiro_digito))

    lista_multiplicada2 = lista_multi(cnpj, soma_cnpj2)
    total_soma_lista2 = soma_lista(lista_multiplicada2)

    segundo_digito = 11 - (total_soma_lista2 % 11)
    if segundo_digito > 9:
        segundo_digito = 0
    else:
        pass

    del(cnpj[-1])

    cnpj.append(str(primeiro_digito))
    cnpj.append(str(segundo_digito))

    cnpj.insert(2, '.')
    cnpj.insert(6, '.')
    cnpj.insert(10, '/')
    cnpj.insert(15, '-')

    novo_cnpj = ''.join(cnpj)

    if novo_cnpj == cnpj_original:
        print('Válido')
        break
    else:
        print('Inválido')
        break













