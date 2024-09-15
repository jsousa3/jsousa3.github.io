preço                = 40
desconto             = 10 # este valor é em percentagem
conversão_euro_dólar = 1.1
conversão_euro_libra = 0.9

def preço_a_pagar(preço, desconto):

    return preço*(1 - desconto/100)

def converter_moeda(preço, conversão):

    return preço * conversão

def valor_do_desconto(preço, desconto):

    return preço * desconto / 100

valor_a_pagar_euros    = preço_a_pagar(preço, desconto)
valor_a_pagar_dólares  = converter_moeda(valor_a_pagar_euros, conversão_euro_dólar)
valor_a_pagar_libras   = converter_moeda(valor_a_pagar_euros, conversão_euro_libra)
valor_desconto_euros   = valor_do_desconto(preço, desconto)
valor_desconto_dólares = converter_moeda(valor_desconto_euros, conversão_euro_dólar)
valor_desconto_libras  = converter_moeda(valor_desconto_euros, conversão_euro_libra)

print('preço do produto:        ', preço, 'em euros')
print('valor do desconto:       ', desconto, 'porcento')
print('preço a pagar em euros:  ', valor_a_pagar_euros)
print('preço a pagar em dólares:', valor_a_pagar_dólares)
print('preço a pagar em libras: ', valor_a_pagar_libras)
print('desconto em euros:       ', valor_desconto_euros)
print('desconto em dólares:     ', valor_desconto_dólares)
print('desconto em libras:      ', valor_desconto_libras)
