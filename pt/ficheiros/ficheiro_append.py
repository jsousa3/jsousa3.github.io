nome_ficheiro = 'exemplo.txt'
modo          = 'a'
ficheiro = open(nome_ficheiro, modo)
uma_string = '''
e esta é uma linha final
(o texto total fica com 5 linhas)'''
ficheiro.write(uma_string)
ficheiro.close()
