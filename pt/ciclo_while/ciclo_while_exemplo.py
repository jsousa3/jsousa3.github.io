
lista_de_descontos = [10, 15, 95, 20, 10, 10, 30, 20, 10, 5]

# indexar uma lista com um ciclo while

contador = 1
índice   = 0
while índice < len(lista_de_descontos):
    print('a executar o corpo do ciclo while')
    print('número de vezes = ', contador )
    desconto = lista_de_descontos[índice]
    print('desconto =', desconto)
    contador = contador + 1
    índice   = índice + 1
print('fim') # esta linha está fora do ciclo while. experimente indentar
             # esta linha. qual é a diferença?
 
