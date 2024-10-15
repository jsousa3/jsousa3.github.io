# uma lista, com listas com listas
lista_de_produtos = [
    [['nome', 'farinha'], ['preço', 1.23], ['desconto', 10], ['em stock', True]],
    [['nome', 'arroz'], ['preço', 0.80], ['desconto', 5], ['em stock', False]]
]

for produto in lista_de_produtos:
    print('produto')
    for campo in produto:
        print('campo')
        for elemento in campo:
            print('elemento', elemento)

# agora com índices
print('''
#############################
##### agora com índices #####
#############################
''')

for índice_produto in range(len(lista_de_produtos)):
    print('produto')
    produto = lista_de_produtos[índice_produto]
    for índice_campo in range(len(produto)):
        print('campo')
        campo = produto[índice_campo]
        for índice_elemento in range(len(campo)):
            elemento = campo[índice_elemento]
            print('elemento', elemento)

