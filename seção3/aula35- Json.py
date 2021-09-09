import json

d1 = {
    'pessoa 1':{
        'nome': 'Lucas',
        'idade': 18,
    },
    'pessoa 2':{
        'nome': 'Elias',
        'idade': 22,

    }
}
d1_json = json.dumps(d1, indent=True)


with open('abc.json', 'w') as file:
    file.write(d1_json)
