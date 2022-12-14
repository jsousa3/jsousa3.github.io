def valor_a_pagar_e_valor_desconto(preco, desconto):

    valor_desconto = preco * desconto/100
    valor_a_pagar  = preco - valor_desconto
    resultado_1      = round(valor_a_pagar, 2)
    resultado_2      = round(valor_desconto, 2)

    resultado = (resultado_1, resultado_2)
    
    return resultado

precos          = [1.23, 7.08, 3.00, 0.53, 2.01, 4.44, 9.99, 2.50, 0.20, 7.70]
descontos       = [8.0 , 5.5 , 3.0 , 3.3 , 9.0 , 9.9 , 2.0 , 2.0 , 5.0 ,  5.0]
valores_a_pagar = [] # inicialmente esta lista está vazia
valores_dos_descontos = [] # inicialmente esta lista está vazia

for indice in range(len(precos)):
    
    preco          = precos[indice]
    desconto       = descontos[indice]
    valores        = valor_a_pagar_e_valor_desconto(preco, desconto)
    # valores é um tuplo. o primeiro elemento é o valor a pagar. o segundo é
    # o valor do desconto
    valor_a_pagar  = valores[0]
    valor_desconto = valores[1]

    valores_a_pagar.append(valor_a_pagar)
    valores_dos_descontos.append(valor_desconto)

print('preços:')
print(precos)
print('descontos:')
print(descontos)
print('valores a pagar:')
print(valores_a_pagar)
print('valores dos descontos:')
print(valores_dos_descontos)
