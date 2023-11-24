nome_ficheiro = 'exemplo.txt'
modo          = 'rb'
ficheiro = open(nome_ficheiro, modo)
bytes = ficheiro.read(1)
while len(bytes) == 1:
    print('byte = ', bytes[0], ' (conversão para letra = ', chr(bytes[0]), ')')
    bytes = ficheiro.read(1)
ficheiro.close()
