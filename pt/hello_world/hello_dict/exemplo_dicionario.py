# nomes_precos é um dicionário
# as chaves são nomes de produtos (strings)
# os valores são os preços dos produtos identiicados pelas chaves
nomes_precos  = {'pão':1.23, 'água':7.08, 'café':3.00, 'sal':0.53}

# valor associado à chave 'sal'
print(nomes_precos['sal'])

# alteração do valor associado à chave 'sal'
nomes_precos['sal'] = 0.55

# percorrer todos os pares chave/valor no dicionário
for chave in nomes_precos:
    valor = nomes_precos[chave]
    print('par chave/valor')
    print(chave)
    print(valor)

# testar se uma chave está no dicionário
nome = 'cacau'
print(nome)
if nome in nomes_precos:
   preco = nomes_precos[nome]
   print(preco)
else:
   print('produto não existente')

# a linha seguinte dá erro porque a chave 'cacau' não está no dicionário
print(nomes_precos['cacau'])
