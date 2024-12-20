
from random import seed
from random import randint
from random import choices
from string import ascii_lowercase
from string import ascii_uppercase
from string import digits

seed(123)

def get_random_code(length):
    
    return ''.join(choices(ascii_lowercase + ascii_uppercase + digits,
                           k=length))

number_of_codes = randint(1100, 1200)

filename = 'ficheiro.txt'
mode     = 'wt'

with open(filename, mode, encoding='utf8') as file:

    for n in range(number_of_codes):

        code = get_random_code(10)
        file.write(code + '\n')
    
