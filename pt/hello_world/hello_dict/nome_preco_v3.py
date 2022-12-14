
def get_preco(nome, nomes_precos):

    if nome in nomes_precos:
        return nomes_precos[nome]
    else:
        return None

# chave: nome de produto
# valor: preço de produto
nomes_precos  = {
    'pão':   1.23,
    'água':  7.08,
    'café':  3.00,
    'sal':   0.53,
    'leite': 2.01,
    'kiwi':  4.44,
    'maça':  9.99,
    'pera':  2.50
    }
    
# testes

def get_mensagem(preco):
    if preco != None:
        return preco
    else:
        return 'preço não existente'

# produtos a listar
produtos = ['pão', 'sal', 'pera', 'cacau']
for produto in produtos:
    preco    = get_preco(produto, nomes_precos)
    mensagem = get_mensagem(preco)
    print(produto)
    print(mensagem)
