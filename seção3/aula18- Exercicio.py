
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

# total = 0
# for produto in carrinho:
#     total = total + produto[1]
# print(total)


total = sum([  y  for x, y in carrinho ])
print(total)