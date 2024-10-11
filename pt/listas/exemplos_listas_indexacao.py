# indexação a patir do princípio da lista

lista_de_preços   = [97, 70, 15, 38, 92, 30, 86, 68, 6, 80]
primeiro_elemento = lista_de_preços[0] # o primeiro elemento está no índice 0
segundo_elemento  = lista_de_preços[1] # o segundo elemento está no índice 1
último_elemnto    = lista_de_preços[9] # como esta lista tem 10 elementos o
                                       # último elemento está no índice 9
				       # (porque os índices começam em zero)
print(lista_de_preços)
print(primeiro_elemento)
print(segundo_elemento)
print(último_elemnto)

# indexação a patir do fim da lista

lista_de_preços    = [97, 70, 15, 38, 92, 30, 86, 68, 6, 80]
último_elemento    = lista_de_preços[-1] # o último elemento está no índice -1
penúltimo_elemento = lista_de_preços[-2] # o penúltimo elemento está no índice -2
primeiro_elemento  = lista_de_preços[-10] # como esta lista tem 10
                                          # elementos, indexando a
                                          # partir do fim, o primeiro
                                          # elemento está no índice
                                          # -10
print(lista_de_preços)
print(último_elemento)
print(penúltimo_elemento)
print(primeiro_elemento)

# erro - elemento não existente - índice fora da gama de índices possíveis

lista_de_preços  = [97, 70, 15, 38, 92, 30, 86, 68, 6, 80]
elementoa         = lista_de_preços[10] # esta linha dá erro. tem que
                                        # ser corrigida. porque não
                                        # existe nenhum elemento no
                                        # índice 10 de uma lista com
                                        # 10 elementos. porque os
                                        # índices começam em zero. o
                                        # índice do último elemento é
                                        # 9
elementob         = lista_de_preços[-11] # esta linha também dá
                                         # erro. tem que ser
                                         # corrigida. porque não
                                         # existe nenhum elemento no
                                         # índice -11 de uma lista com
                                         # 10 elementos. porque os
                                         # índices negativos começam
                                         # em -1. o índice do último
                                         # elemento é -10
print(lista_de_preços)
print(elementoa)
print(elementob)
