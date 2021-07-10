
# t1 = 1,2,3,4,5
# t2 = 6,7,8,9,10
# t3 = t1 + t2
# print(t3,type(t3))

'''
Densempacota em variaveis
'''
# t1 = 1,2,3,4,5
# t2 = 6,7,8,9,10
# t3 = t1 + t2
#
# n1,n2,n3,*resto,n9,n10 = t3
#
# print(*resto,n9,n10)


'''
Modificando o valor de uma Tupla
'''
t1 = (1,2,3,4,5)
t1 = list(t1)
t1[1] = 500
t1 = tuple(t1)

print(t1)