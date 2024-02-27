
class Pessoa:

    def __init__(self, peso, altura):

        self.peso   = peso
        self.altura = altura

    # método para calcular o IMC
    def f(self):

        return self.peso / (self.altura * self.altura)

peso_1   = 80  # em Kg
altura_1 = 1.8 # em metros
pessoa_1 = Pessoa(peso_1, altura_1)

peso_2   = 70  # em Kg
altura_2 = 1.7 # em metros
pessoa_2 = Pessoa(peso_2, altura_2)

print('*** pessoa_1 ***')
print(pessoa_1)
print('*** pessoa_2 ***')
print(pessoa_2)

