def preço_a_pagar(preço, desconto):

    print('a executar a função preço_a_pagar... início')
    fator = desconto/100 # fator do desconto entre zero e um
    valor_do_desconto = preço * fator
    resultado = preço - valor_do_desconto
    print('a executar a função preço_a_pagar... fim')
    return resultado

print('Hello World')

preço_1         = 20
desconto_1      = 10
preço_2         = 40
desconto_2      = 10
preço_1_a_pagar = preço_a_pagar(preço_1, desconto_1) # aqui chama-se a
                                                     # função
preço_2_a_pagar = preço_a_pagar(preço_2, desconto_2) # e aqui chama-se
                                                     # a função outra
                                                     # vez

print(preço_1_a_pagar)
print(preço_2_a_pagar)
