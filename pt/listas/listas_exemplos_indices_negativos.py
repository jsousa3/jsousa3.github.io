lista_de_preços    = [97, 70, 15, 38, 92, 30, 86, 68, 6, 80]
# o último elemento está no índice -1
último_elemento    = lista_de_preços[-1]
# o penúltimo elemento está no índice -2
penúltimo_elemento = lista_de_preços[-2]
# como esta lista tem 10 elementos, indexando a partir do fim, o
# primeiro elemento está no índice -10
primeiro_elemento  = lista_de_preços[-10] 
print(lista_de_preços)
print(último_elemento)
print(penúltimo_elemento)
print(primeiro_elemento)
# a linha que se segue dá erro. tem que ser corrigida. numa lista com
# 10 elementos não existe o elemento no índice -11
elemento = lista_de_preços[-11]
print(elemento)
