def preço_a_pagar(preço, desconto): # esta linha é o cabeçalho da função

    print('a executar a função preço_a_pagar... início')
    print('o valor do argumento preço é   :', preço)
    print('o valor do argumento desconto é:', desconto)
    fator = desconto/100 # fator do desconto entre zero e um
    valor_do_desconto = preço * fator
    resultado = preço - valor_do_desconto
    return resultado
    # o próximo print nunca é executado porque está depois do return
    print('a executar a função preço_a_pagar... fim')

def hello():
    
    print('Hello World')
    # como esta função não tem return, retorna None

preço_1         = 20
desconto_1      = 10
preço_2         = 40
desconto_2      = 10
preço_1_a_pagar = preço_a_pagar(preço_1, desconto_1) # aqui chama-se a
                                                     # função
preço_2_a_pagar = preço_a_pagar(preço_2, desconto_2) # e aqui chama-se
                                                     # a função outra
                                                     # vez
hello()
print(preço_1_a_pagar)
print(preço_2_a_pagar)
hello()

auxiliar = hello()
print(auxiliar)
