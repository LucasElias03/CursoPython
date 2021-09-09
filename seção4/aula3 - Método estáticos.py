'''
Método estático - Uma função normal dentro de uma classe.
'''

from random import randint

class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def ano_nascimento(self):
        print( self.ano_atual - self.idade)

    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand


p1 = Pessoa('Lucas', 18)
p1.ano_nascimento()
print(p1.gera_id())
print(Pessoa.gera_id())