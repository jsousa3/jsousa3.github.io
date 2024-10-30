# uma lista com listas
tabela = [
    [0, 2, 0, 0, 0],
    [3, 0, 7, 0, 9],
    [1, 0, 5, 0, 1]
]
print(tabela)

for linha in tabela:
    print('linha =', linha)
    for valor in linha:
        print('valor =', valor)

# agora com índices
print('''
#############################
##### agora com índices #####
#############################
''')

for índice_linha in range(len(tabela)):
    linha = tabela[índice_linha ]
    print('linha =', linha)
    for índice_coluna in range(len(linha)):
        valor = linha[índice_coluna]
        print('valor =', valor)

