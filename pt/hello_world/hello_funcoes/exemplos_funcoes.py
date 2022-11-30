# definição de uma função com dois argumentos
def mostra_valores(preco, desconto):

    valor_desconto = preco * desconto/100
    valor_preco    = preco - valor_desconto
    print(round(valor_preco, 2))
    print(round(valor_desconto, 2))

# definição de uma função sem argumentos
def hello():

    print('Hello World')

# chamada a uma função sem argumentos
hello()
# chamada a uma função com dois argumentos
mostra_valores(0.78, 5.5)
