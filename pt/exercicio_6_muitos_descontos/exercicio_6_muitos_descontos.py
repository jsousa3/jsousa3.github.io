def calcula_preço_a_pagar(preço, desconto):

    return preço * (1.0 - desconto/100)

# os valores dos descontos são em percentagem

lista_de_preços    = [97, 70, 15, 38, 92, 30, 86, 68, 6,  80]
lista_de_descontos = [10, 15, 5,  25, 10, 10, 35, 25, 10, 5]

for índice in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    preço         = lista_de_preços[índice]
    desconto      = lista_de_descontos[índice]
    preço_a_pagar = calcula_preço_a_pagar(preço, desconto)
    print(preço_a_pagar)
