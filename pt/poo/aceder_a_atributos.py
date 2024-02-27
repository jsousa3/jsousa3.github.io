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

class Pessoa:

    def __init__(self, peso, altura):

        self.peso   = peso
        self.altura = altura

    # método para calcular o IMC
    def f(self):

        return self.peso / (self.altura * self.altura)

    
preco_1    = 10
desconto_1 = 10 # por cento
produto_1  = Produto(preco_1, desconto_1)

preco_2    = 20
desconto_2 = 5 # por cento
produto_2  = Produto(preco_2, desconto_2)

peso_1   = 80  # em Kg
altura_1 = 1.8 # em metros
pessoa_1 = Pessoa(peso_1, altura_1)

peso_2   = 70  # em Kg
altura_2 = 1.7 # em metros
pessoa_2 = Pessoa(peso_2, altura_2)

print('***** produto 1 *****')
# acesso aos membros - atributos que armazenam os dados do objeto. são valores
preco         = produto_1.atributo_preco
desconto      = produto_1.atributo_desconto
# acesso aos métodos (neste caso só há um, f) - atributos que efetuam
# operações sobre os dados do objeto. são funções
valor_a_pagar = produto_1.f()
print('preço         =', preco)
print('desconto      =', desconto)
print('valor a pagar =', valor_a_pagar)

print('***** produto 2 *****')
# acesso aos membros - atributos que armazenam os dados do objeto. são valores
preco         = produto_2.atributo_preco
desconto      = produto_2.atributo_desconto
# acesso aos métodos (neste caso só há um, f) - atributos que efetuam
# operações sobre os dados do objeto. são funções
valor_a_pagar = produto_2.f()
print('preço         =', preco)
print('desconto      =', desconto)
print('valor a pagar =', valor_a_pagar)

print('***** pessoa 1 *****')
# acesso aos membros - atributos que armazenam os dados do objeto. são valores
peso   = pessoa_1.peso
altura = pessoa_1.altura
# acesso aos métodos (neste caso só há um, f) - atributos que efetuam
# operações sobre os dados do objeto. são funções
imc    = pessoa_1.f()
print('peso   =', peso)
print('altura =', altura)
print('imc    =', imc)

print('***** pessoa 2 *****')
# acesso aos membros - atributos que armazenam os dados do objeto. são valores
peso   = pessoa_2.peso
altura = pessoa_2.altura
# acesso aos métodos (neste caso só há um, f) - atributos que efetuam
# operações sobre os dados do objeto. são funções
imc    = pessoa_2.f()
print('peso   =', peso)
print('altura =', altura)
print('imc    =', imc)
