def desconto_quantidade(quantidade):
    if quantidade > 10:
        desconto = 20 # em percentagem
    elif quantidade > 5:
        desconto = 10 # em percentagem
    else:
        desconto = 2 # em percentagem
    return desconto # esta linha está fora do else. é sempre
                    # executada, incondicionalmente

print(desconto_quantidade(15)) # apesar de 15 ser maior que 10 e
                               # também ser maior que 5, só um dos
                               # ramos é que é executado. o primeiro
                               # em que a condição correpondente seja
                               # verdadeira. mesta caso, o ramo
                               # correspondente a quantidade > 10
print(desconto_quantidade(7))
print(desconto_quantidade(3))
