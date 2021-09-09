'''
Uma superclasse genérica, e suas subclasses serão mais específicas. Além disso, ela não pode ser instanciada.
'''

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod # Todas as classe que herde de A tenha o metodo (falar).
    def falar(self):
        pass


class B(A):
    def falar(self):
        print('Falando... B...')





a = B()
a.falar()


