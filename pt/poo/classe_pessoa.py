
class Pessoa:

    def __init__(self, peso, altura):

        self.peso   = peso
        self.altura = altura

    # método para calcular o IMC
    def f(self):

        return self.peso / (self.altura * self.altura)
    
