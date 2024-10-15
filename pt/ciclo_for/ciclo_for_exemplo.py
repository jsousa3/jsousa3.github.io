contador = 1
for preço in [97, 70, 15, 38, 92, 30, 86, 68, 6, 80]:
    print('a executar o corpo do ciclo for')
    print('número de vezes = ', contador )
    print('preço =', preço)
    contador = contador + 1
print('fim') # esta linha está fora do ciclo for. experimente indentar
             # esta linha. qual é a diferença?
print(preço) # a variável do ciclo fica definida e com o último valor
             # da sequência
