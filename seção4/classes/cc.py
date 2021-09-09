from seção4.classes.conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agercia, conta, saldo, limite=100):
        super().__init__(agercia, conta, saldo,)
        self._limite = limite

    @property
    def limite(self):
        return self._limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        self.saldo = self.saldo - valor
        self.detalhes()

