'''
Sobreposição de membros
'''

class A:
    def a(self):
        print('Na classe A')


class B(A):
    def a(self):
        print('Na classe B')


class C(B):
    def a(self):
        A.a(self)
        super().a()
        print('Na classe C')


c = C()
c.a()








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

    def falar(self):
        print('Estou em CLIENTE')


class ClienteVIP(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print(f'{self.nome} {self.sobrenome}')



c1 = ClienteVIP('Lucas', 18, 'ELias')
c1.falar()
