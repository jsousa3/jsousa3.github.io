lista_de_preços    = [97, 70, 15, 38, 92, 30, 86, 68, 6,  80]
lista_de_descontos = [10, 15, 5,  25, 10, 10, 35, 25, 10, 5]

for índice in range(len(lista_de_preços)):

    print('índice =', índice)
    preço = lista_de_preços[índice]
    desconto = lista_de_descontos[índice]
    print('preço =', preço, 'desconto =', desconto)
