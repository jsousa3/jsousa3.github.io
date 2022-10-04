def mostra_valor(preco, desconto):
    # o argumento desconto é em percentagem

    # resolvemos alterar a forma como calculamos os valores
    valor_desconto = preco * desconto/100
    valor_preco    = preco - valor_desconto
    print(round(valor_preco, 2))

preco_chocolate = 1.27
desconto_1      = 7.0  # desconto em percentagem para quantidade = 1
desconto_2      = 11.0 # desconto em percentagem para quantidade = 2

quantidade = 1

if quantidade == 1:
    desconto = desconto_1
    mensagem = 'na compra de 1 chocolate o valor a pagar é:'
else:
    desconto = desconto_2
    mensagem = 'na compra de 2 chocolates o valor a pagar por cada um é:'
    
print(mensagem)
mostra_valor(preco_chocolate, desconto)
