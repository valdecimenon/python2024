# Conversão de inteiro para binário

# obtém o código ASCII 
inteiro = ord('A')  #65

# Primeiro método: usando bin()
binario = bin(inteiro)  # 0b1000001
print(binario)
print('Valor binário:', binario[2:])

# Segundo método: usando format()
binario = format(inteiro, 'b')
print(binario)

# Conversão de binário em inteiro
binario = '1000001'
# converte a string a partir da base 2 em inteiro
inteiro = int(binario, 2)
print(inteiro)

# Rolagem de bits para a esquerda: <<
num = 5
resultado = num << 1 # desloca os bits para esq. 1 posição
print(resultado)

# Rolagem de bits para a direita: >>
num = 20
resultado = num >> 1 # desloca os bits para dir. 1 posição
print(resultado)

#===== Criptografia com Algoritmo RSA ====

import rsa

pubkey, privkey = rsa.newkeys(512)


# texto para criptografar
texto = "as águas dos rios correm para o grande oceano"

#codifica para UTF-8  e criptografa
criptografado = rsa.encrypt(texto.encode(), pubkey)
print(criptografado)

#decriptografa texto e decodifica de utf-8
descriptografado = rsa.decrypt(criptografado, privkey).decode()
print(descriptografado)

