def calcula_preço_a_pagar(preço, desconto):

    return preço * (1.0 - desconto/100)

# os valores dos descontos são em percentagem

lista_de_preços    = [97, 70, 15, 38, 92, 30, 86, 68, 6,  80]
lista_de_descontos = [10, 15, 5,  25, 10, 10, 35, 25, 10, 5]

# daqui para baixo o programa funciona para qualquer número de
# produtos. não tem que ser alterado se o número de produtos variar

print('número de produtos:', len(lista_de_preços))

for índice in range(len(lista_de_preços)):
    print(índice)
    preço         = lista_de_preços[índice]
    desconto      = lista_de_descontos[índice]
    preço_a_pagar = calcula_preço_a_pagar(preço, desconto)
    print(preço_a_pagar)
