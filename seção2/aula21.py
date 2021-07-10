
secreto = 'computador'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você Perdeu')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Digite apenas uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra segreta')
    else:
        print(f'A letra "{letra}" NÃO EXISTE na palavra segreta')
        digitadas.pop()

    secreta_temporaria = ''
    for letra_segreta in secreto:
        if letra_segreta in digitadas:
            secreta_temporaria = secreta_temporaria + letra_segreta
        else:
            secreta_temporaria = secreta_temporaria + '*'

    if secreta_temporaria == secreto:
        print()
        print(f'Parabens voce ganhou a palavra era "{secreto}".')
        break
    else:
        print(secreta_temporaria)

    if letra not in secreto:
        chances = chances - 1

    print(f'Você ainda tem "{chances}" chances')







