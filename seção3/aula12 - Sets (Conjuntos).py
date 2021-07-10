'''
add - (adicionar)
update - (atualizar) itera sobre o elemento
discard - (discartar) remover um valor
union, | - (une) dois conjuntos
intersection, & - (Todos os elementos presentes nos dois sets(conjuntos))
difference, - - (Elementos apenas no set da esquerda)
symmetric_difference, ^ - (Elementos que estão nos dois sets, mais nao em ambos)
'''



# s1 = {1,2,3,4,5}
# s2 = set()
# s2.add(1)
# s2.add(2)
#
# print(s1)
# print(s2)



# s1 = {1,2,3,4,5,7}
# s2 = {1,2,3,4,5,6,}
# s3 = s1.union(s2)
#
# print(s3)




l1 = ['Lucas', 'João', 'Maria']
l2 = ['João', 'Maria', 'Lucas', 'Lucas',
                    'Maria', 'Maria','Maria','Maria']

if set(l1) == set(l2):
    print('l1 e igual a l2')
else:
    print('l1 não e igual a l2')
