def mostra_valores(preco, desconto):
    valor_desconto = preco * desconto/100
    valor_a_pagar  = preco - valor_desconto
    print('-----')
    print('preço')
    print(preco)
    print('desconto')
    print(desconto)
    print('valor a pagar')
    print(round(valor_a_pagar, 2))
    print('valor do desconto')
    print(round(valor_desconto, 2))

preco    = 1.23
desconto = 8.0
mostra_valores(preco, desconto)

preco    = 7.08
desconto = 5.5
mostra_valores(preco, desconto)

preco    = 3.00
desconto = 3.0
mostra_valores(preco, desconto)

preco    = 0.53
desconto = 3.3
mostra_valores(preco, desconto)

preco    = 2.01
desconto = 9.0
mostra_valores(preco, desconto)

preco    = 4.44
desconto = 9.9
mostra_valores(preco, desconto)

preco    = 9.99
desconto = 2.0
mostra_valores(preco, desconto)

preco    = 2.50
desconto = 2.0
mostra_valores(preco, desconto)

preco    = 0.20
desconto = 5.0
mostra_valores(preco, desconto)

preco    = 7.70
desconto = 5.0
mostra_valores(preco, desconto)
