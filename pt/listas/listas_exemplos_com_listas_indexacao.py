# uma lista, com listas com listas
lista_de_produtos = [
    [['nome', 'farinha'], ['preço', 1.23], ['desconto', 10], ['em stock', True]],
    [['nome', 'arroz'], ['preço', 0.80], ['desconto', 5], ['em stock', False]]
]
print(lista_de_produtos)
print(lista_de_produtos[0]) # lista_de_produtos[0] é uma lista. logo pode ser indexada
print(lista_de_produtos[0][0]) # lista_de_produtos[0][0] é uma lista. logo pode ser in                            
print(lista_de_produtos[0][0][0]) # finalmente lista_de_produtos[0][0][0] é uma string
# outros exemplos
print(lista_de_produtos)
print(lista_de_produtos[1])
print(lista_de_produtos[1][1])                
print(lista_de_produtos[1][1][1])
# outros exemplos
print(lista_de_produtos)
print(lista_de_produtos[1])
print(lista_de_produtos[1][2])                
print(lista_de_produtos[1][2][1])
# outros exemplos
print(lista_de_produtos)
print(lista_de_produtos[-1])
print(lista_de_produtos[-1][-1])                
print(lista_de_produtos[-1][-1][-1])
# alternativa
print(lista_de_produtos)
produto_1 = lista_de_produtos[0] # farinha
print(produto_1)
produto_1_campo_3 = produto_1[2] # desconto
print(produto_1_campo_3)
produto_1_campo_3_valor = produto_1_campo_3[1] # valor do desconto
print(produto_1_campo_3_valor)
