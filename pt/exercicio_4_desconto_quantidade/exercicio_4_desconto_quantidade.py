def desconto_em_percentagem(quantidade):

    if quantidade == 1:
        return 10
    elif quantidade == 2:
        return 20
    elif quantidade == 3:
        return 30
    else:
        return 40

def valor_a_pagar(preço, quantidade):

    desconto             = desconto_em_percentagem(quantidade)
    desconto_por_unidade = preço*desconto/100
    resultado            = (preço - desconto_por_unidade) * quantidade
    return resultado

preço           = 40
quantidade_1    = 1
valor_a_pagar_1 = valor_a_pagar(preço, quantidade_1)
quantidade_2    = 2
valor_a_pagar_2 = valor_a_pagar(preço, quantidade_2)
quantidade_3    = 3
valor_a_pagar_3 = valor_a_pagar(preço, quantidade_3)
quantidade_4    = 4
valor_a_pagar_4 = valor_a_pagar(preço, quantidade_4)
quantidade_5    = 5
valor_a_pagar_5 = valor_a_pagar(preço, quantidade_5)

desconto_1 = desconto_em_percentagem(quantidade_1)
desconto_2 = desconto_em_percentagem(quantidade_2)
desconto_3 = desconto_em_percentagem(quantidade_3)
desconto_4 = desconto_em_percentagem(quantidade_4)
desconto_5 = desconto_em_percentagem(quantidade_5)

print('preço do produto:', preço)
print('quantidade:      ', quantidade_1)
print('desconto:        ', desconto_1, '%')
print('valor a pagar:   ', valor_a_pagar_1)
print('quantidade:      ', quantidade_2)
print('desconto:        ', desconto_2, '%')
print('valor a pagar:   ', valor_a_pagar_2)
print('quantidade:      ', quantidade_3)
print('desconto:        ', desconto_3, '%')
print('valor a pagar:   ', valor_a_pagar_3)
print('quantidade:      ', quantidade_4)
print('desconto:        ', desconto_4, '%')
print('valor a pagar:   ', valor_a_pagar_4)
print('quantidade:      ', quantidade_5)
print('desconto:        ', desconto_5, '%')
print('valor a pagar:   ', valor_a_pagar_5)
