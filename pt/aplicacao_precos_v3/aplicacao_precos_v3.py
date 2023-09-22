
def calcula_valor_desconto(preco, desconto):
    # o desconto é em percentagem
    return preco*desconto/100

def calcula_preco_a_pagar(preco, desconto):
    # o desconto é em percentagem
    desconto_absoluto = calcula_valor_desconto(preco, desconto)
    return preco - desconto_absoluto

def converte_preco(preco_em_euros, fator_conversao):

    return preco_em_euros * fator_conversao

preco    = 20
desconto = 10 # este valor é em percentagem
fator_euro_dolar = 1.1
fator_euro_libra = 0.9

preco_a_pagar_em_euros = calcula_preco_a_pagar(preco, desconto)
desconto_em_euros      = calcula_valor_desconto(preco, desconto)

print('preço a pagar em euros')
print(preco_a_pagar_em_euros)
print('preço a pagar em dólares')
print(converte_preco(preco_a_pagar_em_euros, fator_euro_dolar))
print('preço a pagar em libras')
print(converte_preco(preco_a_pagar_em_euros, fator_euro_libra))
print('desconto em euros')
print(desconto_em_euros)
print('desconto em dólares')
print(converte_preco(desconto_em_euros, fator_euro_dolar))
print('desconto em libras')
print(converte_preco(desconto_em_euros, fator_euro_libra))
