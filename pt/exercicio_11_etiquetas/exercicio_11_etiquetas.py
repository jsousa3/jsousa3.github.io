
preço_eur = 20
desconto  = 10    # este valor é em percentagem
eur_jpy   = 150.0 # jpy - Japanese Yen

def converte(preço, fator_de_conversão):

    return preço * fator_de_conversão

def preço_a_pagar(preço, desconto):

    return preço * (100 - desconto)/100

def etiqueta(preço_eur, desconto, eur_jpy):
    
    preço_jpy = converte(preço_eur, eur_jpy)
    preço_a_pagar_eur = preço_a_pagar(preço_eur, desconto)
    preço_a_pagar_jpy = preço_a_pagar(preço_jpy, desconto)

    # códigos
    eur = 'EUR'
    jpy = 'JPY'
    separador = '*************************'
    
    resultado = f'''{separador}
* {eur:^8} * {jpy:^10} *
{separador}
* {preço_eur:^8.2f} * {preço_jpy:^10.2f} *
{separador}
* {desconto/100:^21.0%} *
{separador}
* {preço_a_pagar_eur:^8.2f} * {preço_a_pagar_jpy:^10.2f} *
{separador}'''
    
    return resultado

etiqueta_1 = etiqueta(preço_eur, desconto, eur_jpy)
print(etiqueta_1)
