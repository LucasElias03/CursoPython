

class CarinhoDeCompra:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.preco)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.preco
        return total



class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco












carrinho = CarinhoDeCompra()

p1 = Produto('Camiseta', 50)
p2 = Produto('Celular', 1000)
p3 = Produto('Violão', 120)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p2)
carrinho.inserir_produto(p3)

carrinho.lista_produto()
print(carrinho.soma_total())





