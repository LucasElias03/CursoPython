from aula6_associacao import Escritor
from aula6_associacao import Caneta
from aula6_associacao import MaquinaDeEscreve

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscreve()
escritor.ferramenta = caneta
escritor.ferramenta.escrever()

