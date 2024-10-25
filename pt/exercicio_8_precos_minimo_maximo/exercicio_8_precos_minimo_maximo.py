
def get_minimo_e_maximo(lista):

    mínimo = lista[0]
    máximo = lista[0]

    for número in lista:

        if número < mínimo:
            mínimo = número

        if número > máximo:
            máximo = número

    resultado = [mínimo, máximo] # uma lista com dois elementos

    return resultado
    
lista_de_preços = [97, 70, 15, 38, 92, 30, 86, 68, 6,  80]

lista_mínimo_máximo = get_minimo_e_maximo(lista_de_preços)

preço_mínimo = lista_mínimo_máximo[0]
preço_máximo = lista_mínimo_máximo[1]

print('preço mínimo =', preço_mínimo)
print('preço máximo =', preço_máximo)
