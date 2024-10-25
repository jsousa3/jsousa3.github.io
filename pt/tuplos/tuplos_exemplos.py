
# tuplos

mínimo = 5
máximo = 31

# criar 
resultado = (mínimo, máximo) # um tuplo com dois elementos

print('resultado =', resultado)

# indexar

primeiro_elemento = resultado[0]
segundo_elemento  = resultado[1]

print('primeiro elemento =', primeiro_elemento)
print('segundo  elemento =', segundo_elemento)

# indexar com um ciclo for

print('índice valor')
for índice in range(len(resultado)):
    elemento = resultado[índice]
    print(índice, elemento)

# comprimento (número de elemento)

print('número de elemento de resultado =', len(resultado))

# alterar - NÃO SE PODE - DÁ ERRO - OS TUPLOS SÃO IMUTÁVEIS

resultado[0] = 7 # esta linha tem que ser comentada porque dá
                 # erro. não se pode alterar um tuplo. é imutável
