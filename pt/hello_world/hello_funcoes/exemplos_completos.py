def mostra_valores(preco, desconto):

    valor_desconto = preco * desconto/100
    valor_preco    = preco - valor_desconto
    print(round(valor_preco, 2))
    print(round(valor_desconto, 2))
 
def hello():

    print('Hello World')

hello()
mostra_valores(0.78, 5.5)
