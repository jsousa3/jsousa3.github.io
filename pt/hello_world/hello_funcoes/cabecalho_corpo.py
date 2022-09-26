def mostra_valores(preco, desconto):        # esta linha é o cabeçalho

    valor_desconto = preco * desconto/100   # estas 
    valor_preco    = preco - valor_desconto # linhas
    print(round(valor_preco, 2))            # são
    print(round(valor_desconto, 2))         # o corpo
