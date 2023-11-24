nome_ficheiro = 'exemplo.txt'
modo          = 'r'
ficheiro = open(nome_ficheiro, modo)
n_linha = 1
for linha in ficheiro:
    print('linha', n_linha, ' = "', linha, '"')
    n_linha = n_linha + 1
ficheiro.close()
