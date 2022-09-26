def mostra_valor_a_pagar(preco, quantidade, desconto_1, desconto_2):

    desconto = desconto_1     # assume-se que a quantidade é 1
    if quantidade == 2:       # se a quntidade for 2
        desconto = desconto_2 # altera-se o desconto para desconto_2

    valor_desconto = preco * desconto/100
    valor_a_pagar  = preco - valor_desconto
    print(round(valor_a_pagar, 2))
