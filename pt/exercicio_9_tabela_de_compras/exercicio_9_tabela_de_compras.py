
# função para criar uma tabela
def cria_tabela():

    tabela = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    return tabela

# função para fazer output de uma tabela
def mostra_tabela(tabela):

    for índice_linha in range(3):
        linha = tabela[índice_linha]
        print(linha)

# função para retornar o número numa linha e coluna de uma tabela
def retorna_valor(tabela, número_linha, número_coluna):

    índice_linha  = número_linha - 1
    índice_coluna = número_coluna - 1

    valor = tabela[índice_linha][índice_coluna]
   
    return valor

# função para guardar numa linha e coluna um valor
def altera_valor(tabela, número_linha, número_coluna, valor):

    índice_linha  = número_linha - 1
    índice_coluna = número_coluna - 1

    tabela[índice_linha][índice_coluna] = valor

# exeplos
tabela = cria_tabela()
print('tabela')
mostra_tabela(tabela)
print('valores iniciais')
valor_2_1 = retorna_valor(tabela, 2, 1)
print('linha', 2, 'coluna', 1, 'valor', valor_2_1)
valor_1_2 = retorna_valor(tabela, 1, 2)
print('linha', 1, 'coluna', 2, 'valor', valor_1_2)
print('a alterar valores...')
altera_valor(tabela, 2, 1, 3)
altera_valor(tabela, 1, 2, 2)
print('a alterar valores... fim.')
print('valores alterados')
valor_2_1 = retorna_valor(tabela, 2, 1)
print('linha', 2, 'coluna', 1, 'valor', valor_2_1)
valor_1_2 = retorna_valor(tabela, 1, 2)
print('linha', 1, 'coluna', 2, 'valor', valor_1_2)
print('tabela')
mostra_tabela(tabela)
