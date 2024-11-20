moeda                   = 'EUR'
preço                   = 20
desconto_em_percentagem = 10
preço_a_pagar           = 18
s1 = f'''
moeda:         {moeda}
preço:         {preço:.1f}
desconto:      {desconto_em_percentagem:.5f}%
preço a pagar: {preço_a_pagar:.2f}
'''
print(s1)
