perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2? ',
        'resposta': {'a': '1','b': '4','c': '5'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'resposta': {'a': '4', 'b': '10', 'c': '6'},
        'resposta_certa': 'c',
    },
}
print()
respotas_certas = 0
for chave_p, valor_p in perguntas.items():
    print(f'{chave_p}: {valor_p["pergunta"]}')
    print('Respostas:')

    for chave_r, valor_r in valor_p['resposta'].items():
        print(f'[{chave_r}]: {valor_r}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == valor_p['resposta_certa']:
        print('Você Acertou !!!')
        respotas_certas += 1
    else:
        print('Você Errou !!!')

    print()
qnt_pergunta = len(perguntas)
porcentagem_acerto = respotas_certas / qnt_pergunta * 100

print(f'Você acertou {respotas_certas} pergunta')
print(f'Sua porcentagem de acertos foi de {porcentagem_acerto}%')
