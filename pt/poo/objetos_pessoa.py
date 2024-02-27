
class Pessoa:

    def __init__(self, peso, altura):

        self.peso   = peso
        self.altura = altura

    # método para calcular o IMC
    def f(self):

        return self.peso / (self.altura * self.altura)

peso_1   = 80  # em Kg
altura_1 = 1.8 # em metros
pessoa_1 = Pessoa(peso_1, altura_1) # pessoa_1 é um novo valor do tipo
                                    # Pessoa. é um objeto

peso_2   = 70  # em Kg
altura_2 = 1.7 # em metros
pessoa_2 = Pessoa(peso_2, altura_2) # pessoa_2 é um novo valor do tipo
                                    # Pessoa. é um objeto

# ambos os objetos têm os mesmos atributos:
# atributos que armazenam valores:
#  - peso,
#  - altura
# atributo para executar operações (sobre os valores armazenados):
#  - f

# mas os valores dos atributos armazenados em cada objeto são diferentes
# no objeto pessoa_1 o peso é 80 e a altura é 1.8
# no objeto pessoa_2 o peso é 70 e a altura é 1.7
