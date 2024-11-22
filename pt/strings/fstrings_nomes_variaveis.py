moeda                   = 'EUR'
preço                   = 20
desconto_em_percentagem = 0.1
preço_a_pagar           = 18

# sem f-strings
print('moeda =', moeda)
print('preço =', preço)
print('desconto_em_percentagem =', desconto_em_percentagem)
print('preço_a_pagar =', preço_a_pagar)

# com f-strings (esta versão dá muito menos trabalho a escrever)
print(f'{moeda = }')
print(f'{preço = }')
print(f'{desconto_em_percentagem = }')
print(f'{preço_a_pagar = }')
