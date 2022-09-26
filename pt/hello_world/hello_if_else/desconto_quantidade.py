def mostra_valor_a_pagar(preco, quantidade, desconto_1, desconto_2):

    if quantidade == 1:
        desconto = desconto_1
    else:
        desconto = desconto_2

    valor_desconto = preco * desconto/100
    valor_a_pagar  = preco - valor_desconto
    print(round(valor_a_pagar, 2))

preco_chocolate = 1.27
desconto_1      = 7.0  # desconto em percentagem para quantidade = 1
desconto_2      = 11.0 # desconto em percentagem para quantidade = 2

quantidade = 1
print('na compra de 1 chocolate o valor a pagar é:')
mostra_valor_a_pagar(preco_chocolate, quantidade, desconto_1, desconto_2)

quantidade = 2
print('na compra de 2 chocolates o valor a pagar por cada um é:')
mostra_valor_a_pagar(preco_chocolate, quantidade, desconto_1, desconto_2)
