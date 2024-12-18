
lista_de_descontos = [40, 30, 30, 20, 20, 20, 10, 40, 30, 10, 50]

def está_na_lista(elemento, lista):

    for elemento_na_lista in lista:
        if elemento_na_lista == elemento:
            return True
    return False

def retirar_repetidos(lista):

    resultado = []

    for elemento in lista:
        if está_na_lista(elemento, resultado) == False:
            resultado.append(elemento)

    return resultado

lista_de_descontos_sem_repetidos = retirar_repetidos(lista_de_descontos)

print(lista_de_descontos_sem_repetidos)
