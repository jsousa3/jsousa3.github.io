
lista_de_descontos = [10, 15, 95, 20, 10, 10, 30, 20, 10, 5]

desconto_grande = 80

índice = 0
existe = False
while existe == False and índice < len(lista_de_descontos):

    desconto = lista_de_descontos[índice]
    
    #print(índice, desconto) # descomente este print só para confirmar
                             # quantas vezes este ciclo while é executado
    if desconto > desconto_grande:
        existe = True

    índice = índice + 1
        
if existe == True:
    print('existe pelo menos um desconto maior que 80%')
else:
    print('não existe nenhum desconto maior que 80%')
