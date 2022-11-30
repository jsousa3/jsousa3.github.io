descontos = [8.0 , 5.5 , 3.0 , 3.3 , 9.0 , 9.9 , 2.0 , 2.0 , 5.0 ,  5.0]

print(descontos)
conjunto = set(descontos)
print(conjunto)
lista_sem_repeticoes = list(conjunto)
print(lista_sem_repeticoes)
# numa única linha
lista_sem_repeticoes = list(set(descontos))
print(lista_sem_repeticoes)
