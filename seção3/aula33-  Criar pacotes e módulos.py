import sercao3_vendas.calculo_preço
from sercao3_vendas import calculo_preço
from sercao3_vendas.calculo_preço import aumento,reducao
#                                   mudando o nome preco para preco2
from sercao3_vendas.formata import preco as preco2

preco = 49.90
preco_com_aumento = sercao3_vendas.calculo_preço.aumento(preco, 15, formata= True)
print(preco_com_aumento)

preco = 49.90
preco_com_reducao = sercao3_vendas.calculo_preço.reducao(preco, 15, formata= True)
print(preco_com_reducao)

print(preco2.real(50.99))
