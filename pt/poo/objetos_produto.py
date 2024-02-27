
class Produto:
    
    def __init__(self, valor_preco, valor_desconto):

        self.atributo_preco    = valor_preco
        self.atributo_desconto = valor_desconto

    # método para calcular o valor a pagar
    def f(self):

        preco    = self.atributo_preco
        desconto = self.atributo_desconto

        valor_desconto = preco * desconto/100
        valor_a_pagar  = preco - valor_desconto

        return valor_a_pagar

preco_1    = 10
desconto_1 = 10 # por cento
produto_1  = Produto(preco_1, desconto_1) # produto_1 é um novo valor
                                          # do tipo Produto. é um
                                          # objeto

preco_2    = 20
desconto_2 = 5 # por cento
produto_2  = Produto(preco_2, desconto_2) # produto_2 é um novo valor
                                          # do tipo Produto. é um
                                          # objeto

# ambos os objetos têm os mesmos atributos:
# atributos que armazenam valores:
#  - atributo_preco,
#  - atributo_desconto
# atributo para executar operações (sobre os valores armazenados):
#  - f

# mas os valores dos atributos armazenados em cada objeto são diferentes
# no produto_1 o preço é 10 e o desconto também é 10
# no produto_2 o preço é 20 e o desconto é 5
