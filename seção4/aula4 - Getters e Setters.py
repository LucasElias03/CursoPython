'''
A ideia dos métodos get e set é permitir que atributos privados da classe possam ser buscados/modificados fora dela.
Get - Busca
Set - Alterar

'''


class Produtos:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.lower()



    # Getter - Vai obter o valor
    @property
    def preco(self):
        return self._preco

    # Setter - Vai configurar o preço.
    @preco.setter #(valor) está se referindo a istancia (preco)._
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor




p1 = Produtos('CAMISETA', 50)
p1.desconto(10)
print(p1.nome, p1.preco)

p2 = Produtos('BONÉ', 'R$100')
p2.desconto(15)
print(p2.nome, p2.preco)
