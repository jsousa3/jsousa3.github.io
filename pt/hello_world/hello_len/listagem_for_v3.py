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

# o último elemento desta duas listas foi removido
precos    = [1.23, 7.08, 3.00, 0.53, 2.01, 4.44, 9.99, 2.50, 0.20]
descontos = [8.0 , 5.5 , 3.0 , 3.3 , 9.0 , 9.9 , 2.0 , 2.0 , 5.0 ]

for indice in range(10):
    preco    = precos[indice]
    desconto = descontos[indice]
    mostra_valores(preco, desconto)
