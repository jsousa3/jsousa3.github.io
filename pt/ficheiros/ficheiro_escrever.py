nome_ficheiro = 'exemplo.txt'
modo          = 'w' # não é necessário usar 'wt' porque t é o modo
                    # pré-definido (default)
ficheiro = open(nome_ficheiro, modo)
uma_string_com_3_linhas = '''exemplo de
texto com
3 linhas'''
ficheiro.write(uma_string_com_3_linhas)
ficheiro.close()
