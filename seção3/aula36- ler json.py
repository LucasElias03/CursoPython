import json
'''
Lendo json
'''
# with open('abc.json', 'r') as file:
#     d1_jason = file.read()
#     print(d1_jason)



'''
Voltou a ser um dicionario
'''
with open('abc.json', 'r') as file:
    d1_jason = file.read()
    d1_jason = json.loads(d1_jason)


for k, v in d1_jason.items():
    print(k)
    for k1, v1 in v.items():
        print(k1,v1)

