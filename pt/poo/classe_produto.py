
# nome da classe: Produto
class Produto:

    # construtor
    # argumentos do construtor:
    # self           - um objeto "vazio" fornecido pelo intrepretador Python
    # valor_preco    - o valor do preço do produto
    # valor_desconto - o valor do desconto a aplicar
    def __init__(self, valor_preco, valor_desconto):

        # criar no objeto vazio, self, o atributo atributo_preco para
        # armazenar o preco. É inicializado com o valor do preco. O
        # acesso aos atributos faz-se com o operador . (ponto)
        self.atributo_preco    = valor_preco
        # criar no objeto vazio, self, o atributo atributo_desconto para
        # armazenar o desconto. É inicializado com o valor do desconto
        self.atributo_desconto = valor_desconto

    # método para calcular o valor a pagar
    # argumentos:
    # apenas o objeto sobre o qual o método é executado, self.
    def f(self):

        # obter os valores do preco e do desconto que estão
        # armazenados nos atributos do objeto
        preco    = self.atributo_preco
        desconto = self.atributo_desconto

        # fazer as contas
        valor_desconto = preco * desconto/100
        valor_a_pagar  = preco - valor_desconto

        # retornar o resultado
        return valor_a_pagar
