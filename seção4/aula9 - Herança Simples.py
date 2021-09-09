class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclass = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclass} está falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nomeclass} comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nomeclass} estudando...')









c1 = Cliente('Lucas', 18)
c1.falar()
c1.comprar()

a1 = Aluno('João', 42)
a1.falar()
a1.estudar()

p1 = Pessoa('Maria', 34)
p1.falar()
