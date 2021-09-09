
lista_a = [1,2,3,4,5,6,7]
lista_b = [1,2,3,4]


# lista_soma = []
# for i in range(len(lista_b)):
#      lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)




lista_soma = []
for i, _ in enumerate(lista_b):
     lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)






# for a,b in zip(lista_a,lista_b):
#     lista_soma = a + b
#     print(lista_soma)





# print([sum(v) for v in zip(lista_a,lista_b)])




#
# lista_soma = [a + b for a,b in zip(lista_a,lista_b)]
# print(lista_soma)
#

