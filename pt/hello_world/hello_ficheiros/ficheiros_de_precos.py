lista_auxiliar = []

nome_do_ficheiro = 'precos.txt'
modo             = 'r'    # leitura. r de read
codificacao      = 'utf8' # isto é necessário em Windows
ficheiro_precos  = open(nome_do_ficheiro, modo, encoding=codificacao)

print('a ler o ficheiro de preços...')
for linha in ficheiro_precos:
    if linha[0] != '0':
       lista_auxiliar.append(linha)
print('a ler o ficheiro de preços... fim!')

ficheiro_precos.close()

nome_do_ficheiro      = 'precos_altos.txt'
modo                  = 'w'    # escrita. w de write
codificacao           = 'utf8' # isto é necessário em Windows
ficheiro_precos_altos = open(nome_do_ficheiro, modo, encoding=codificacao)

print('a escrever o ficheiro de preços altos...')
for linha in lista_auxiliar:
    ficheiro_precos_altos.write(linha)
print('a escrever o ficheiro de preços altos... fim!')

ficheiro_precos_altos.close()
