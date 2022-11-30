def valor_a_pagar(preco, desconto):

    valor_desconto = preco * desconto/100
    valor_a_pagar  = preco - valor_desconto
    resultado      = round(valor_a_pagar, 2)
    
    return resultado

precos          = [1.23, 7.08, 3.00, 0.53, 2.01, 4.44, 9.99, 2.50, 0.20, 7.70]
descontos       = [8.0 , 5.5 , 3.0 , 3.3 , 9.0 , 9.9 , 2.0 , 2.0 , 5.0 ,  5.0]
valores_a_pagar = [] # inicialmente esta lista está vazia

for indice in range(len(precos)):
    
    preco    = precos[indice]
    desconto = descontos[indice]
    valor    = valor_a_pagar(preco, desconto)

    valores_a_pagar.append(valor)

print('preços:')
print(precos)
print('descontos:')
print(descontos)
print('valores a pagar:')
print(valores_a_pagar)
