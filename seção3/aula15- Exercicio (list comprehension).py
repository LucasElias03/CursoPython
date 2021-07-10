
# string = '0123456789012345678901234567890123456789012345678901234567890123456789'
#
# lista = [string[0:10] for v in string]
# retorno = '.'.join(lista)
# print(retorno)


# string = 'ABCDEFGHIJ012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
#
# lista = [string[i:i + 10] for i in range(0, len(string), 10)]
# print('.'.join(lista))




# string = '012345678901234567890123456789012345678901234567890123456789'
# retorno = '.'.join([string[x:x+10] for x in range(0, len(string), 10)])
# print(retorno)



string = '0123456789012345678901234567890123456789012345678901234567890123456789'

for x in range(0,len(string),10):
    lista = (string[x:x+10])
    print(lista)


