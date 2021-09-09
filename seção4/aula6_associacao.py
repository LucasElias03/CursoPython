# ferrameta - Porque ferramenta não é configurada pelo construtor... Provavelmente para adiar a configuração
# de ferramenta para depois, ou para ter a possibilidade de trocar de ferramenta.

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.ferramenta = None

    @property
    def nome(self):
        return self.__nome

    @property
    def ferramenta(self):
        return self.__ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta



class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca

    def escrever(self):
        print('Caneta está escrevendo...')


class MaquinaDeEscreve:
    def escrever(self):
        print('Maquina está escrevendo...')

