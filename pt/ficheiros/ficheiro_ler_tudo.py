nome_ficheiro = 'exemplo.txt'
modo          = 'r'
ficheiro = open(nome_ficheiro, modo)
tudo = ficheiro.read() # ler o ficheiro todo de uma vez
ficheiro.close()
print(tudo)
