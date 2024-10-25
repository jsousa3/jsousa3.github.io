
lista_de_descontos = [10, 15, 95, 20, 10, 10, 30, 20, 10, 5]

desconto_grande = 80

existe = False
for desconto in lista_de_descontos:

    #print(desconto) # descomente este print só para confirmar quantas
                     # vezes este ciclo for é executado
    if desconto > desconto_grande:
        existe = True

if existe == True:
    print('existe pelo menos um desconto maior que 80%')
else:
    print('não existe nenhum desconto maior que 80%')
