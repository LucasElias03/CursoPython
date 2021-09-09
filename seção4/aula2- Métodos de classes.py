'''
Método de Classe -
'''


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def cria_nascimento(cls, nome, ano_nascimento):
        idade2 = cls.ano_atual - ano_nascimento
        return cls(nome, idade2)

p1 = Pessoa.cria_nascimento('Lucas', 2003)
print(p1.nome, p1.idade)

p2 = Pessoa.cria_nascimento('João', 1998)
print(p2.nome, p2.idade)

