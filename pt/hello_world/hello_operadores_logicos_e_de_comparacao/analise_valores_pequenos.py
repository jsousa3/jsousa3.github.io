
precos    = [1.23, 7.08, 3.00, 0.53, 2.01, 4.44, 9.99, 2.50, 0.20, 7.70]
descontos = [8.0 , 5.5 , 3.0 , 3.3 , 9.0 , 9.9 , 2.0 , 2.0 , 5.0 ,  5.0]

print('preços menores que 2.00 e com descontos maiores ou iguais que 5.0%:')
for indice in range(10):

    preco    = precos[indice]
    desconto = descontos[indice]

    if (preco < 2.0) and (desconto >= 5.0):
        print('preço')
        print(preco)
        print('desconto')
        print(desconto)
        print('-----')
