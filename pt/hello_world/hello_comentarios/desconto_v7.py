# dados os valores do preço de um produto e de um desconto (em perentagem),
# este programa mostra o valor a pagar pelo produto, assim como o valor do
# desconto.

preco    = 1.33
desconto = 9    # este desconto é em percentagem.

print(round(preco * (1.0 - desconto/100), 2))
print(round(preco * desconto/100, 2))
