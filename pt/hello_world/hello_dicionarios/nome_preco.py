
def get_preco(nome, lista_nomes, lista_precos):

    indice_produto = None

    for indice in range(len(lista_nomes)):
        if lista_nomes[indice] == nome:
            indice_produto = indice

    if indice_produto != None:
        return lista_precos[indice_produto]
    else:
        return None

nomes  = ['pão', 'água', 'café', 'sal', 'leite', 'kiwi', 'maça', 'pera']
precos = [1.23,  7.08,   3.00,   0.53,  2.01,    4.44,   9.99,   2.50]
    
# testes
produto = 'pão'
preco   = get_preco(produto, nomes, precos)
print(produto)
if preco != None:
    print(preco)
else:
    print('preço não existente')

produto = 'sal'
preco   = get_preco(produto, nomes, precos)
print(produto)
if preco != None:
    print(preco)
else:
    print('preço não existente')

produto = 'pera'
preco   = get_preco(produto, nomes, precos)
print(produto)
if preco != None:
    print(preco)
else:
    print('preço não existente')

produto = 'cacau'
preco   = get_preco(produto, nomes, precos)
print(produto)
if preco != None:
    print(preco)
else:
    print('preço não existente')

