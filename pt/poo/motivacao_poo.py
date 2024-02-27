
# retorna o valor a pagar por um produto, dados um preço e um desconto
# (em percentagem)
def f1(preco, desconto):

    return preco - preco * desconto/100

# retorna o índice de massa corporal de uma pessoa, dados um peso e
# uma altura
def f2(peso, altura):

    # o índice de massa corporal (imc) é dado pelo peso (em Kg) dividido
    # pelo quadrado da altura (em metros)
    # valores entre 18.5 e 24.9 são considerados normais
    return peso/(altura*altura)

# produto 1
preco_1         = 10
desconto_1      = 10
valor_a_pagar_1 = f1(preco_1, desconto_1)
# consumidor 1
peso_1   = 80
altura_1 = 1.7
imc_1    = f2(peso_1, altura_1)
print('***** produto 1 *****')
print('preço         = ', preco_1)
print('desconto (%)  = ', desconto_1)
print('valor a pagar = ', valor_a_pagar_1)
print('***** consumidor 1 *****')
print('peso   = ', peso_1)
print('altura = ', altura_1)
print('imc    = ', imc_1)

# produto 2
preco_2         = 20
desconto_2      = 5
valor_a_pagar_2 = f2(preco_2, desconto_2)
# consumidor 2
peso_2   = 70
altura_2 = 1.75
imc_2    = f1(peso_2, altura_2)
print('***** produto 2 *****')
print('preço         = ', preco_2)
print('desconto (%)  = ', desconto_2)
print('valor a pagar = ', valor_a_pagar_2)
print('***** consumidor 2 *****')
print('peso   = ', peso_2)
print('altura = ', altura_2)
print('imc    = ', imc_2)
