# from itertools import groupby
#
# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Lucas', 'nota': 'B'},
#     {'nome': 'Letícia', 'nota': 'A'},
#     {'nome': 'Fabrício', 'nota': 'C'},
#     {'nome': 'Rose', 'nota': 'D'},
#     {'nome': 'Joana', 'nota': 'A'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'C'},
#     {'nome': 'José', 'nota': 'B'}
# ]
#
# alunos.sort(key= lambda item : item['nota'])
# grupo_aluno = groupby(alunos,lambda item : item['nota'])
# for grupo,aluno_agrupados in grupo_aluno:
#     print()
#
#     print(f'Grupo: {grupo}')
#     for aluno in aluno_agrupados:
#         print(aluno)
#     print()
#
#     # print(f'{len(list(aluno_agrupados))} alunos tiraram nota {grupo}')







from itertools import groupby

pessoas = [
    {'nome': 'luiz', 'idade': 30},
    {'nome': 'joão', 'idade': 20},
    {'nome': 'maria', 'idade': 40},
    {'nome': 'helena', 'idade': 21},
    {'nome': 'rosana', 'idade': 20},
    {'nome': 'osvaldo', 'idade': 21},
    {'nome': 'eleonor', 'idade': 40},
]

def retorna_idade(pessoa):
    return pessoa['idade']

ordenadas_por_idade = sorted(pessoas, key=retorna_idade)
ordenadas_por_idade = groupby(pessoas, key=retorna_idade)

for idade, grupo in ordenadas_por_idade:
    print(f'Grupos de pessoas com {idade}:')

    for pessoas in grupo:
        print(pessoas)



