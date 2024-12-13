
lista_códigos      = ['USD', 'JPY', 'GBP', 'CHF', 'BRL']
lista_taxas_câmbio = [1.0527, 159.74, 0.82555, 0.9267, 6.3811]

def retorna_índice(código_moeda, lista_códigos):

    resultado = None

    for índice in range(len(lista_códigos)):
        código_na_lista = lista_códigos[índice]
        if código_na_lista == código_moeda:
            resultado = índice
            
    return resultado

# na próxima linha python pode substituir-se GBP por qualquer um dos
# códigos na lista lista_códigos
índice_taxa     = retorna_índice('GBP', lista_códigos)
taxa_pretendida = lista_taxas_câmbio[índice_taxa]
print(taxa_pretendida)
