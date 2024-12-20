
nome_do_ficheiro = 'ficheiro.txt'
modo             = 'rt' # read, text mode
codificação      = 'utf8'

lista_de_linhas = []

with open(nome_do_ficheiro, modo, encoding=codificação) as ficheiro:

    for linha in ficheiro:

        lista_de_linhas.append(linha)

# índices das linhas
índice_1 = 0      # primeira linha
índice_2 = -1     # última linha
índice_3 = 354-1  # linha 354
índice_4 = 721-1  # linha 721
índice_5 = 1027-1 # linha 1027

print(lista_de_linhas[índice_1])
print(lista_de_linhas[índice_2])
print(lista_de_linhas[índice_3])
print(lista_de_linhas[índice_4])
print(lista_de_linhas[índice_5])
