from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agercia, conta, saldo):
        self._agercia = agercia
        self._conta = conta
        self._saldo = saldo

    @property
    def agercia(self):
        return self._agercia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa se um númerico')
        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor do depositor precisa se númerico')
        self._saldo = self._saldo + valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência:{self._agercia}', end=' ')
        print(f'Conta:{self._conta}', end=' ')
        print(f'Saldo:{self._saldo}')

    @abstractmethod
    def sacar(self,valor):
        pass