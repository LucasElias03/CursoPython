
tarefa_lista = []
refazer_lista = []

while True:
    tarefa = input('Digite uma tarefa ou undo, redo, ls: ')

    if tarefa == 'ls':
        print()
        print('Tarefas:')
        print(tarefa_lista)
        print()
        continue
    elif tarefa == 'undo':
        if not tarefa_lista:
            print('Nada a desfazer')
        else:
            nova_lista = tarefa_lista.pop()
            refazer_lista.append(nova_lista)
        continue
    elif tarefa == 'redo':
        if not tarefa_lista:
            print('Nada a refazer')
        else:
            nova_lista = refazer_lista.pop()
            tarefa_lista.append(nova_lista)
        continue


    tarefa_lista.append(tarefa)