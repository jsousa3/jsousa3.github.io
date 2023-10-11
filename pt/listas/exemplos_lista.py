# uma lista com um número inteiro, uma string,
# e um boleano
uma_lista = [10, 'hello', False]
print(uma_lista)
print('primeiro elemento')
print(uma_lista[0])
print('segundo elemento')
print(uma_lista[1])
print('terceiro elemento')
print(uma_lista[2])
print('acrescentar um float no fim')
uma_lista.append(2.0)
print(uma_lista)
print('inserir uma string no terceiro elemento')
uma_lista.insert(2, 'world')
print(uma_lista)
print('remover o primeiro elemento')
uma_lista.pop(0)
print(uma_lista)
print('número de elemntos da lista')
print(len(uma_lista))
# a próxima linha dá erro, porque o elemento quinto não existe
print(uma_lista[4])
