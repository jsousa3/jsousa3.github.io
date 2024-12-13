# dicionário de taxas de câmbios:
# - chaves: códigos de moeda
# - valores: taxas de câmbio
taxas_câmbio = {'USD':1.0527, 'JPY':159.74, 'GBP':0.82555, 'CHF':0.9267, 'BRL':6.3811}

# na próxima linha python pode substituir-se GBP por qualquer um dos
# códigos no dicionário taxas_câmbio
taxa_pretendida = taxas_câmbio['GBP']
print(taxa_pretendida)
