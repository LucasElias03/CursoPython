'''
Polimorfismo é o principio que permite que classes derivadas de uma mesma superclasse tenhamétodos iguais
(de mesma assinatura) mas comportamento diferente.
Mesma assinatura = Mesma quantidade e tipo parâmetros
'''
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def falar(self, msg):
        pass

class B(A):
    def falar(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def falar(self, msg):
        print(f'C está falando {msg}')


b = B()
c = C()
b.falar('UM ASSUNTO')
c.falar('OUTRO ASSUNTO')
