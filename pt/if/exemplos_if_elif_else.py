# experimenta executar este programa alterando o valor da variável
# quandidade
quantidade = 3 # experimente, por exemplo, -1, 0, 1, 2, 10, 100

if quantidade == 1: # condição 1
    # bloco associado à condição 1
    desconto = 10
    print('o desconto aplicado é:', desconto, '%')
elif quantidade == 2: # condição 2
    # bloco associado à condição 2
    desconto = 20
    print('o desconto aplicado é:', desconto, '%')
elif quantidade == 3: # condição 3
    # bloco associado à condição 3
    desconto = 30
    print('o desconto aplicado é:', desconto, '%')
else:
    # bloco executado caso todas as condições sejam falsas
    desconto = 40
    print('o desconto aplicado é:', desconto, '%')
