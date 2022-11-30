def valor_a_pagar(preco, desconto):

    if desconto == 0.0:
        print('nada a calcular')
        return preco

    print('a calcular o valor a pagar...')
    valor_desconto = preco * desconto/100
    valor_a_pagar  = preco - valor_desconto
    resultado      = round(valor_a_pagar, 2)
    print('a calcular o valor a pagar... fim!')
    
    return resultado

preco_chocolate    = 1.23
desconto_chocolate = 8.0
valor_chocolate    = valor_a_pagar(preco_chocolate, desconto_chocolate)
print('valor chocolate =')
print(valor_chocolate)

preco_saco    = 0.10
desconto_saco = 0.0
valor_saco    = valor_a_pagar(preco_saco, desconto_saco)
print('valor saco =')
print(valor_saco)

