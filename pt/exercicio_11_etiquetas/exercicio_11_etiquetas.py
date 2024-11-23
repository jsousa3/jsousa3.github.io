
código_eur        = 'EUR'
código_jpy        = 'JPY'
preço_eur         = 20
preço_jpy         = 3000
desconto          = 10    # este valor é em percentagem
valor_a_pagar_eur = 18
valor_a_pagar_jpy = 2700

def retorna_etiqueta(código_moeda_1,
                     código_moeda_2,
                     preço_moeda_1,
                     preço_moeda_2,
                     desconto,
                     valor_a_pagar_modeda_1,
                     valor_a_pagar_modeda_2):
    
    resultado = f'''*************************
* {código_moeda_1:^8} * {código_moeda_2:^10} *
*************************
* {preço_moeda_1:^8.2f} * {preço_moeda_2:^10.2f} *
*************************
* {desconto/100:^21.0%} *
*************************
* {valor_a_pagar_modeda_1:^8.2f} * {valor_a_pagar_modeda_2:^10.2f} *
*************************'''
    
    return resultado

etiqueta = retorna_etiqueta(código_eur, código_jpy,
                            preço_eur, preço_jpy,
                            desconto,
                            valor_a_pagar_eur, valor_a_pagar_jpy)
print(etiqueta)

