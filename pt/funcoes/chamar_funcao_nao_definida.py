preço_1         = 20
desconto_1      = 10
# a linha que se segue dá erro. porque a função preço_a_pagar ainda
# não está definida
preço_1_a_pagar = preço_a_pagar(preço_1, desconto_1)

print(preço_1_a_pagar)

# o nome desta função é preço_a_pagar
# os argumentos da função são preço e desconto

def preço_a_pagar(preço, desconto): # esta linha é o cabeçalho da função

    # as próximas 6 linhas Python são o corpo da função
    # quando a função é chamada o corpo da função é executado

    print('a executar a função preço_a_pagar... início')
    
    fator = desconto/100 # fator do desconto entre zero e um
    
    valor_do_desconto = preço * fator

    resultado = preço - valor_do_desconto
    
    print('a executar a função preço_a_pagar... fim')

    return resultado

print('Hello World') # esta linha não faz parte da função. por isso
                     # não é executada quando a função é
                     # executada/chamada
