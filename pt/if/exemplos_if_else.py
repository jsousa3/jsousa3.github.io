def login(password_fornecida, password_armazenada):
    print('Início de login...')
    if password_fornecida == password_armazenada:
        print('Bem vindo!')
        print('Fez login com sucesso.')
    else:
        print('Password incorreta.')
        print('Tente novamente.')
    print('Fim de login.') # esta linha está fora do else. é sempre
                           # executada, incondicionalmente
    
password_armazenada = 'portugal'
print('Primeira tentativa')
password_fornecida  = 'espanha'
login(password_fornecida, password_armazenada)
print('Segunda tentativa')
password_fornecida  = 'portugal'
login(password_fornecida, password_armazenada)
