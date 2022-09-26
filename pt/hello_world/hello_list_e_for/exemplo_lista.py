uma_lista = [1.0, 'hello', 2.0, 'world'] # isto é uma lista
print(uma_lista[0])                      # este é o primeiro elemento
indice = 1
print(uma_lista[indice])                 # este é o segundo elemento
indice = 2
print(uma_lista[indice])                 # este é o terceiro elemento
print(uma_lista[3])                      # este é o quarto elemento

# alterar o terceiro elemento
uma_lista[2] = 'python'

print(uma_lista)

# o quinto elemento não existe
# a próxima linha dá erro
print(uma_lista[4])
