preço                = 40
desconto             = 10 # este valor é em percentagem
conversão_euro_dólar = 1.1
conversão_euro_libra = 0.9
print('preço do produto:        ', preço, 'em euros')
print('valor do desconto:       ', desconto, 'porcento')
print('preço a pagar em euros:  ', preço - preço*desconto/100)                        # preço a pagar em euros
print('preço a pagar em dólares:', (preço - preço*desconto/100)*conversão_euro_dólar) # preço a pagar em dólares
print('preço a pagar em libras: ', (preço - preço*desconto/100)*conversão_euro_libra) # preço a pagar em libras
print('desconto em euros:       ', preço*desconto/100)                                # desconto em euros
print('desconto em dólares:     ', preço*desconto/100*conversão_euro_dólar)           # desconto em dólares
print('desconto em libras:      ', preço*desconto/100*conversão_euro_libra)           # desconto em libras