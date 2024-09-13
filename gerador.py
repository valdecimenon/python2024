# Gerador de senha

import random
import string

tamanho = int(input('Digite o tamanho da senha desejada: '))


#abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_letters)

#0123456789
print(string.digits)

# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
print(string.punctuation)

# Define os caracteres que podem ser usados na senha
caracteres = string.ascii_letters + string.digits + string.punctuation

# Gera uma senha aleatórioa com o tamanjo especificado
"""
for i in range(tamanho):   
    letra = random.choice(caracteres)
    print(letra)
"""

senha = "".join(random.choice(caracteres) for i in range(tamanho))
print('Senha gerada:', senha)