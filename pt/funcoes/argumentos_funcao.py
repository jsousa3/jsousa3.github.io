# o nome desta função é preço_a_pagar
# os argumentos da função são preço e desconto

def preço_a_pagar(preço, desconto): # esta linha é o cabeçalho da função

    # as próximas 6 linhas Python são o corpo da função
    # quando a função é chamada o corpo da função é executado

    print('a executar a função preço_a_pagar... início')

    print('o valor do argumento preço é   :', preço)
    print('o valor do argumento desconto é:', preço)
    
    fator = desconto/100 # fator do desconto entre zero e um
    
    valor_do_desconto = preço * fator

    resultado = preço - valor_do_desconto
    
    print('a executar a função preço_a_pagar... fim')

    return resultado

def hello():
    
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
hello()
print(preço_1_a_pagar)
print(preço_2_a_pagar)
hello()

preço_3         = 20
preço_3_a_pagar = preço_a_pagar(preço_3) # esta linha dá erro. falta
                                         # um argumento. o desconto

hello(10) # esta linha dá erro. a função hello não tem argumentos. não
          # pode receber valores
