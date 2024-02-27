
class Produto:

    def __init__(self, nome, preco, desconto):

        self.nome     = nome
        self.preco    = preco
        self.desconto = desconto

    def __repr__(self):

        return self.nome + ', preço = ' + str(self.preco) + ', desconto = ' \
            + str(self.desconto) + ', valor a pagar = ' \
            + str(self.valor_a_pagar())
        
    def valor_a_pagar(self):

        return self.preco - self.preco*self.desconto/100

class ListaDeCompras:

    def __init__(self, nome):

        self.nome   = nome
        self. lista = []

    def acrescenta_produto(self, produto):

        self.lista.append(produto)

    def __repr__(self):

        resultado = 'Lista de compras: ' + self.nome + '\n'

        for produto in self.lista:

            resultado = resultado + str(produto) + '\n'

        return resultado

    def soma_lista(self, outra_lista):

        resultado = ListaDeCompras('nome criado automaticamente')

        for produto in self.lista:

            resultado.acrescenta_produto(produto)
        
        for produto in outra_lista.lista:

            resultado.acrescenta_produto(produto)

        return resultado

lista_de_comidas = ListaDeCompras('comidas')
p1 = Produto('pão',      1.0, 10)
p2 = Produto('manteiga', 3.0, 10)
lista_de_comidas.acrescenta_produto(p1)
lista_de_comidas.acrescenta_produto(p2)
print(lista_de_comidas)

lista_de_bebidas = ListaDeCompras('bebidas')
p3 = Produto('água',     0.5, 5)
p4 = Produto('leite',    1.1, 5)
lista_de_bebidas.acrescenta_produto(p3)
lista_de_bebidas.acrescenta_produto(p4)
print(lista_de_bebidas)

lista_total = lista_de_comidas.soma_lista(lista_de_bebidas)
print(lista_total)

