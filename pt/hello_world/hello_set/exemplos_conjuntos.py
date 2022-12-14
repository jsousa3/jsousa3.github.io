# criar um conjunto
produtos_loja_1 = {'chocolate', 'água', 'café', 'chocolate'}
# criar outro conjunto
produtos_loja_2 = {'pão', 'água', 'café', 'pão'}
# criar um dicionário (só para comparação)
nomes_precos  = {'pão':1.23, 'água':7.08, 'café':3.00, 'sal':0.53}

# x é um dicionário vazio
x = {}
# y é um conjunto vazio
y = set()

# os elementos repetidos não aparecem no output porque eles não
# existem em conjuntos
print(produtos_loja_1)
print(produtos_loja_2)

# relação de pertença
print('chocolate pertence ao conjunto produtos_loja_1?')
print('chocolate' in produtos_loja_1)
# relação de inclusão
print('o conjunto {água, café} está contido no conjunto produtos_loja_1?')
print({'água', 'café'} <= {'chocolate', 'água', 'café', 'chocolate'})
# conjunto de todos os produtos
uniao = produtos_loja_1 | produtos_loja_2
# produtos vendidos em ambas as lojas
intersecao = produtos_loja_1 & produtos_loja_2
# produtos exclusivos da loja 1
diferenca = produtos_loja_1 - produtos_loja_2
# produtos exclusivos na loja 1 ou na loja 2
diferenca_exclusiva = produtos_loja_1 ^ produtos_loja_2

print('------')
print(uniao)
print(intersecao)
print(diferenca)
print(diferenca_exclusiva)

print(produtos_loja_1[0])
