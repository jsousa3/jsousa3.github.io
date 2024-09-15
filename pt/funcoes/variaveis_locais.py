mensagem = 'Hello World'

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
    
    print(mensagem) # esta linha não dá erro. está definida uma
                    # variável global com o nome mensagem. as
                    # variáveis globais podem ser udsadas no corpo das
                    # funções.

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

# estas duas linhas dão erro. Não há nenhuma variável global com o
# nome preço. Nem nenhuma com o nome fator. as variáveis preço e fator
# são locais à função preço_a_pagar. só podem ser usadas no corpo da
# função
print(preço)
print(fator)
