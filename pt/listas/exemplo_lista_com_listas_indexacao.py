# uma lista cujos elementos são listas
uma_lista = [[1, 2, 3], ['a', 'b', 'c'], [True, 'hello', -2.0]]
print(uma_lista)
auxiliar = uma_lista[1] # este elemento é a lista ['a', 'b', 'c']
print(auxiliar)
auxiliar = auxiliar[2] # este elemento é a string 'c'
print(auxiliar)
# a dupla indexação pode ser efetuada numa única instrução
# uma_lista[1] é uma lista que pode ser indexada para obter-se o
# terceiro elemento, no índice 2
auxiliar = uma_lista[1][2]
print(auxiliar)
