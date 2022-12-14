# Este progrma usa o preço de um produto e um desconto em
# percentagem, para calcular e mostrar o valor a pagar pelo produto, e
# o valor do desconto.

preco    = 1.33
desconto = 9.0 # este desconto é em percentagem.

print(round(preco * (1.0 - desconto/100), 2))
print(round(preco * desconto/100, 2))
