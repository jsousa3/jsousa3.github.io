def mostra_valores(preco, desconto):
    # resolvemos alterar a fórmula como calculamos os valores
    # desconto é em percentagem
    valor_desconto = preco * desconto/100
    valor_preco    = preco - valor_desconto
    print(round(valor_preco, 2))
    print(round(valor_desconto, 2))

# chocolate
preco_chocolate    = 1.33
desconto_chocolate = 9.0    # este desconto é em percentagem.
mostra_valores(preco_chocolate, desconto_chocolate)

# água
preco_agua    = 0.78
desconto_agua = 5.5    # este desconto é em percentagem.
mostra_valores(preco_agua, desconto_agua)
