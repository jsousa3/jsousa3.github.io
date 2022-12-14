# precos é uma lista
precos = [1.23, 7.08, 3.00, 0.53, 2.01, 4.44, 9.99, 2.50, 0.20, 7.70]

print(precos[0])                      # este é o primeiro elemento
indice = 1
print(precos[indice])                 # este é o segundo elemento
indice = 2
print(precos[indice])                 # este é o terceiro elemento
print(precos[3])                      # este é o quarto elemento

# alterar o terceiro elemento
precos[2] = 'esgotado'

print('aqui está a lista completa')
print(precos)

# o décimo primeiro elemento não existe
print(precos[10]) # esta linha dá erro
