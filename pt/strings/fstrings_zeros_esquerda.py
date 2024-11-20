moeda                   = 'EUR'
preço                   = 20
desconto_em_percentagem = 10
preço_a_pagar           = 18
s1 = f'''
moeda:         {moeda:10}
preço:         {preço:010.1f}
desconto:      {desconto_em_percentagem:010.5f}%
preço a pagar: {preço_a_pagar:010.2f}
'''
print(s1)
