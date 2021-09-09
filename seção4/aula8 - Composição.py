class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self,cidade, estado):
        self.cidade = cidade
        self.estado = estado







cliente1 = Cliente('Lucas', 18)
cliente1.inserir_endereco('Vieirópolis', 'PB')
print(cliente1.nome)
cliente1.lista_endereco()
print()
cliente2 = Cliente('João', 33)
cliente2.inserir_endereco('João Pessoa', 'PB')
print(cliente2.nome)
cliente2.lista_endereco()
print()
cliente3 = Cliente('Maria', 52)
cliente3.inserir_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_endereco()



