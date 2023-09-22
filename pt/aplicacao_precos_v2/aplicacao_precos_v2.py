
preco    = 3.27
desconto = 9 # este valor é em percentagem
fator_euro_dolar = 1.07
fator_euro_libra = 0.86

print('preço a pagar em euros')
print(preco - preco*desconto/100)
print('preço a pagar em dólares')
print((preco - preco*desconto/100)*fator_euro_dolar)
print('preço a pagar em libras')
print((preco - preco*desconto/100)*fator_euro_libra)
print('desconto em euros')
print(preco*desconto/100)
print('desconto em dólares')
print(preco*desconto/100*fator_euro_dolar)
print('desconto em libras')
print(preco*desconto/100*fator_euro_libra)
