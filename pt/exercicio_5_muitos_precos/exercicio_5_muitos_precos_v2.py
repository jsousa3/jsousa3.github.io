def preço_a_pagar(preço, desconto):

    return preço * (1.0 - desconto/100)

desconto = 10 # este valor é em percentagem

lista_de_preços = [97, 70, 15, 38, 92, 30, 86, 68, 6, 80]

for preço in lista_de_preços:
    valor_preço_a_pagar = preço_a_pagar(preço, desconto)
    print(valor_preço_a_pagar)
