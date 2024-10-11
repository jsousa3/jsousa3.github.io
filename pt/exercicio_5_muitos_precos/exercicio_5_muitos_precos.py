def preço_a_pagar(preço, desconto):

    return preço * (1.0 - desconto/100)

desconto = 10 # este valor é em percentagem

preço_a_pagar_1  = preço_a_pagar(97, desconto)
preço_a_pagar_2  = preço_a_pagar(70, desconto)
preço_a_pagar_3  = preço_a_pagar(15, desconto)
preço_a_pagar_4  = preço_a_pagar(38, desconto)
preço_a_pagar_5  = preço_a_pagar(92, desconto)
preço_a_pagar_6  = preço_a_pagar(30, desconto)
preço_a_pagar_7  = preço_a_pagar(86, desconto)
preço_a_pagar_8  = preço_a_pagar(68, desconto)
preço_a_pagar_9  = preço_a_pagar(6,  desconto)
preço_a_pagar_10 = preço_a_pagar(80, desconto)

print(preço_a_pagar_1)
print(preço_a_pagar_2)
print(preço_a_pagar_3)
print(preço_a_pagar_4)
print(preço_a_pagar_5)
print(preço_a_pagar_6)
print(preço_a_pagar_7)
print(preço_a_pagar_8)
print(preço_a_pagar_9)
print(preço_a_pagar_10)
