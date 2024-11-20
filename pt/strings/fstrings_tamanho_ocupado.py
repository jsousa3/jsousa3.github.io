moeda                   = 'EUR'
preço                   = 20
desconto_em_percentagem = 10
preço_a_pagar           = 18
s1 = f'''
moeda:         {moeda:10}
preço:         {preço:10.1f}
desconto:      {desconto_em_percentagem:10.5f}%
preço a pagar: {preço_a_pagar:10.2f}
'''
print(s1)
