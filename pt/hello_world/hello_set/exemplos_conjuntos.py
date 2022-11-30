produtos_loja_1 = {'chocolate', 'água', 'café', 'chocolate'}
produtos_loja_2 = {'pão', 'água', 'café', 'pão'}

# conjunto de todos os produtos
uniao = produtos_loja_1 | produtos_loja_2
# produtos vendidos em ambas as lojas
intersecao = produtos_loja_1 & produtos_loja_2
# produtos exclusivos da loja 1
diferenca = produtos_loja_1 - produtos_loja_2
# produtos exclusivos na loja 1 ou na loja 2
diferenca_exclusiva = produtos_loja_1 ^ produtos_loja_2

print(produtos_loja_1)
print(produtos_loja_2)
print('------')
print(uniao)
print(intersecao)
print(diferenca)
print(diferenca_exclusiva)
