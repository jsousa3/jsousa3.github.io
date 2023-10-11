def mensagens(preco_a_pagar, desconto):
    print('Detalhes da sua compra')
    print('Preço a pagar:')
    print(preco_a_pagar)
    if desconto > 0:
        print('Desconto que obteve nesta compra:')
        print(desconto)
    print('Até à próxima') # esta linha está fora do if. é sempre
                           # executada, incondicionalmente
    

print('compra 1')
preco_a_pagar = 5
desconto      = 0
mensagens(preco_a_pagar, desconto)
print('compra 2')
preco_a_pagar = 10
desconto      = 1
mensagens(preco_a_pagar, desconto)
